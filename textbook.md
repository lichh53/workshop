---
title: 数值模拟相关基础技能
author: 中山大学-土木工程学院
date: \today
documentclass: article
fontsize: 12pt
linestretch: 1.5
header-includes:
  - \usepackage{fontspec}
  - \usepackage[UTF8]{ctex}
  - \usepackage{verbatim}
  - \usepackage{titlesec}
  - \usepackage{xcolor,sectsty}
  - \usepackage{enumitem}
  - \usepackage{tabularx}
  - \usepackage{latexsym}
  - \usepackage{marvosym}
  - \usepackage[empty]{fullpage}
  - \usepackage[bookmarksopen=true]{hyperref}
  - \usepackage[normalem]{ulem}
  - \usepackage[english]{babel}
  - \usepackage[default]{sourcesanspro}
  - \urlstyle{same}
  - \definecolor{astral}{RGB}{46,116,181}
  - \subsectionfont{\color{astral}}
  - \sectionfont{\color{astral}}
  - \setmainfont{Arial}
  - \setCJKmainfont{KaiTi}
---

# 第一章：介绍

- 介绍本课程的目标和内容
- 分享一些关于数值模拟和编程的背景知识
- 讨论学生预期获得的技能和知识

# 第二章：Linux 入门

- Linux 操作系统的基础知识，包括文件系统、命令行界面等
- 常用的文本编辑器 Vim 的使用方法
- Shell 编程基础

# 第三章：C++ 基础

- C++ 的核心概念，如变量、数据类型、运算符等
- 控制流语句，如 if 语句、循环语句等
- 函数和递归的基础知识
- 数组和指针等数据结构的基础知识

# 第四章：C++ 高级特性

- 面向对象编程的基础，包括类和对象、继承、多态等
- 模板元编程的基础，包括模板类、模板函数等

# 第五章：CMake 入门

- 介绍 CMake 的概念和用途
- 如何创建 CMakeLists.txt 文件以及执行构建过程

# 第六章：Git 版本控制

- 理解 Git 的基本原理和术语
- 使用 Git 来管理代码版本
- 使用 GitHub 进行协作开发和团队合作

[Link: 06_git/git_main.md](06_git/git_main.md)

# 第七章：数值计算和算法

- 数值计算中常见的线性代数问题，如矩阵操作、特征值计算等
- 常见的数值优化算法，如梯度下降法、共轭梯度法等
- 常见的数值微分和积分算法，如有限差分法、辛普森法等

# 第八章：OpenMP 并行计算

- 理解 OpenMP 的并行化概念和编程模型
- 使用 OpenMP API 来实现并行化计算
- 调试和优化 OpenMP 并行程序

# 第九章：MPI 并行计算

- 理解 MPI 的并行化概念和编程模型
- 使用 MPI API 来实现分布式内存并行计算
- 了解 MPI 程序的调试和性能分析工具

# 第十章：超算入门

- 简要介绍超级计算机的工作原理和架构以及常见术语
- 介绍如何访问并使用超级计算机，比如登录到超算，提交作业等
- 了解资源调度器 Slurm 和任务调度器 PBS 的基本操作

# 第十一章：Matlab 入门

- Matlab 编程语言的基本语法和语句
- Matlab 中的数学计算和数据可视化技术
- 常见工具箱（如信号处理、图像处理等）的使用

# 第十二章：ParaView 可视化

- 介绍 ParaView 的基础概念和功能
- 如何使用 ParaView 来可视化科学计算数据
- ParaView 中高级可视化技术的应用

# 第十三章：LaTeX 与 Markdown 写作

- LaTeX 的基本概念和语法
- 如何使用 LaTeX 来撰写科学研究论文和报告
- 经典数学公式、图表等在 LaTeX 中的排版方法

# 第十四章：项目实践

- 将之前所学知识应用到一个实际项目中
- 学生将要使用超级计算机来解决一个科学计算问题，并编写 C++ 和 Matlab 代码来实现
- 最终的成果将是一个能够运行在超级计算机上的完整的数值模拟和编程项目，包括 OpenMP 和 MPI 并行计算、Git 版本控制、ParaView 可视化和 LaTeX 写作部分。
