import os, re, argparse


def get_md_files(root_dir):
    """
    Recursively find and return a list of all markdown (.md) files in a directory.

    :param root_dir: The root directory to start searching from.
    :return: List of markdown file paths.
    """
    md_files = []

    # Walk through the directory tree
    for root, dirs, files in os.walk(root_dir):
        # Check each file in the current directory
        for file in files:
            if file.endswith(".md"):
                # Add the full path of the markdown file
                md_files.append(os.path.join(root, file))

    return md_files


def get_md_content(file_path):
    """Reads the content of a markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def replace_links(content, md_files, base_dir):
    """
    Replace [Link: <file_path>](<file_path>) lines with the content of
      the corresponding markdown files recursively.

    :param content: The string content of a markdown file.
    :param md_files: List of markdown file paths.
    :param base_dir: The base directory to resolve relative paths.
    :return: Updated content with the Link links replaced.
    """
    keyword_pattern = r"\[Link: ([^\]]+)\]\([^\)]+\)"  # Regex to capture "Link" markdown links

    def resolve_file_path(file_reference):
        """Resolve the file path based on the base directory."""
        return os.path.join(base_dir, file_reference)

    while re.search(keyword_pattern, content):
        # Find all occurrences of 'Link' links
        matches = re.findall(keyword_pattern, content)

        for file_reference in matches:
            # Resolve the file path
            file_path = resolve_file_path(file_reference)

            # Check if the file exists and is in the list of markdown files
            if file_path in md_files:
                # Read the content of the referenced markdown file
                file_content = get_md_content(file_path)

                # Recursively replace "Link" links in the file content
                file_content = replace_links(
                    file_content, md_files, os.path.dirname(file_path)
                )

                # Replace the "Link" line in the original content with the file's content
                content = re.sub(
                    rf"\[Link: {re.escape(file_reference)}\]\([^\)]+\)",
                    file_content,
                    content,
                    count=1,
                )
            else:
                print(f"Warning: Markdown file '{file_reference}' not found.")

    return content


def process_markdown_file(md_file_path, root_dir):
    """
    Process a markdown file, replacing [Go to: ...](...) links with content from the referenced markdown files.

    :param md_file_path: Path to the markdown file to be processed.
    :param root_dir: The root directory containing all markdown files.
    :return: The processed content of the markdown file.
    """
    # Get the list of all markdown files in the directory
    md_files = get_md_files(root_dir)

    # Read the main markdown file content
    main_content = get_md_content(md_file_path)

    # Replace Go to links in the content
    updated_content = replace_links(main_content, md_files, root_dir)

    return updated_content


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

    # Get the list of all markdown files in the directory
    md_files = get_md_files(args.root_dir)

    # Read the main markdown file content
    main_content = get_md_content(args.md_file_path)

    # Replace Go to links in the content
    updated_content = replace_links(main_content, md_files, args.root_dir)

    # Save the updated content to the output file
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Processed content saved to {args.output_file}")


if __name__ == "__main__":
    main()
