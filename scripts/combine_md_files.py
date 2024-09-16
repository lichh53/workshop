import os, re, argparse


def get_md_content(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def resolve_file_path(file_reference, base_dir):
    return os.path.join(base_dir, file_reference)


def extract_file_dir(file_path):
    file_dir = os.path.dirname(file_path)
    return file_dir


def replace_links(content, base_dir):
    keyword_pattern = r"\[Link: ([^\]]+)\]\([^\)]+\)"

    while re.search(keyword_pattern, content):
        matches = re.findall(keyword_pattern, content)

        for file_reference in matches:
            file_path = resolve_file_path(file_reference, base_dir)
            file_base_dir = extract_file_dir(file_path)
            file_content = get_md_content(file_path)

            file_content = replace_links(file_content, file_base_dir)

            content = re.sub(
                rf"\[Link: {re.escape(file_reference)}\]\([^\)]+\)",
                file_content,
                content,
                count=1,
            )

            print(f"Processed file: {file_path}")

    return content


def main():
    """
    Main function to process a markdown file and replace Go to links with content from referenced files.
    Takes three arguments from the command line: the markdown file path, the root directory, and the output file path.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Process a markdown file and replace 'Go to' links with referenced content."
    )
    parser.add_argument(
        "md_file_path", type=str, help="Path to the markdown file to process"
    )
    parser.add_argument(
        "root_dir", type=str, help="Root directory containing markdown files"
    )
    parser.add_argument(
        "output_file", type=str, help="Path to save the processed markdown file"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Read the main markdown file content
    main_content = get_md_content(args.md_file_path)

    # Replace Go to links in the content
    updated_content = replace_links(main_content, args.root_dir)

    # Save the updated content to the output file
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Processed content saved to {args.output_file}")


if __name__ == "__main__":
    main()
