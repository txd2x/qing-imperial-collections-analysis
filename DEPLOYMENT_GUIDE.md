# GitHub Deployment Guide
# GitHub 部署指南

[English](#english) | [中文](#中文)

---

## English

### Prerequisites

1. **GitHub Account**: Create an account at [github.com](https://github.com) if you don't have one
2. **Git Installed**: Install Git on your local machine
   - Windows: Download from [git-scm.com](https://git-scm.com/)
   - Mac: `brew install git`
   - Linux: `sudo apt-get install git` or `sudo yum install git`

### Step 1: Create a New Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the repository details:
   - **Repository name**: `qing-imperial-collections-analysis`
   - **Description**: "Comparative visualization and analysis of Yongzheng and Qianlong imperial collections"
   - **Visibility**: Choose "Public" or "Private"
   - **DO NOT** initialize with README, .gitignore, or license (we already have these files)
5. Click **"Create repository"**

### Step 2: Initialize Local Git Repository

Open your terminal and navigate to the project directory:

```bash
cd /home/sandbox/qing-imperial-collections-analysis
```

Initialize Git repository:

```bash
git init
```

### Step 3: Add Files to Git

Add all files to the staging area:

```bash
git add .
```

Create the initial commit:

```bash
git commit -m "Initial commit: Qing imperial collections comparative analysis"
```

### Step 4: Connect to GitHub Repository

Add the remote repository (replace `YOUR_USERNAME` with your GitHub username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/qing-imperial-collections-analysis.git
```

### Step 5: Push to GitHub

Push your code to GitHub:

```bash
git branch -M main
git push -u origin main
```

**Note**: You may be prompted to enter your GitHub credentials. If you have two-factor authentication enabled, you'll need to use a Personal Access Token instead of your password.

### Step 6: Verify Deployment

1. Go to your repository URL: `https://github.com/YOUR_USERNAME/qing-imperial-collections-analysis`
2. Verify that all files are uploaded correctly
3. Check that the README.md displays properly on the repository homepage

### Optional: Create GitHub Pages (for Documentation)

1. Go to your repository on GitHub
2. Click **"Settings"** tab
3. Scroll down to **"Pages"** section
4. Under **"Source"**, select **"main"** branch and **"/ (root)"** folder
5. Click **"Save"**
6. Your documentation will be available at: `https://YOUR_USERNAME.github.io/qing-imperial-collections-analysis/`

### Optional: Add Topics and Description

1. Go to your repository homepage
2. Click the gear icon ⚙️ next to "About"
3. Add topics (tags):
   - `qing-dynasty`
   - `imperial-collections`
   - `data-visualization`
   - `chinese-art-history`
   - `epigraphy`
   - `python`
   - `matplotlib`
4. Add website URL if you created GitHub Pages
5. Click **"Save changes"**

### Troubleshooting

#### Authentication Issues

If you encounter authentication problems:

1. **Create a Personal Access Token**:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Click "Generate new token"
   - Select scopes: `repo` (full control of private repositories)
   - Copy the token

2. **Use the token as password** when pushing to GitHub

#### Large File Issues

If you have files larger than 100MB:

1. Use Git LFS (Large File Storage):
   ```bash
   git lfs install
   git lfs track "*.png"
   git add .gitattributes
   git commit -m "Add Git LFS tracking"
   ```

---

## 中文

### 前置要求

1. **GitHub 账户**: 如果没有账户，请在 [github.com](https://github.com) 创建
2. **安装 Git**: 在本地机器上安装 Git
   - Windows: 从 [git-scm.com](https://git-scm.com/) 下载
   - Mac: `brew install git`
   - Linux: `sudo apt-get install git` 或 `sudo yum install git`

### 步骤 1: 在 GitHub 上创建新仓库

1. 访问 [github.com](https://github.com)
2. 点击右上角的 **"+"** 图标
3. 选择 **"New repository"**（新建仓库）
4. 填写仓库详情:
   - **Repository name**（仓库名称）: `qing-imperial-collections-analysis`
   - **Description**（描述）: "雍正帝与乾隆帝帝室收藏比较可视化分析"
   - **Visibility**（可见性）: 选择 "Public"（公开）或 "Private"（私有）
   - **不要**勾选初始化 README、.gitignore 或 license（我们已经有这些文件）
5. 点击 **"Create repository"**（创建仓库）

### 步骤 2: 初始化本地 Git 仓库

打开终端并导航到项目目录:

```bash
cd /home/sandbox/qing-imperial-collections-analysis
```

初始化 Git 仓库:

```bash
git init
```

### 步骤 3: 添加文件到 Git

将所有文件添加到暂存区:

```bash
git add .
```

创建初始提交:

```bash
git commit -m "Initial commit: Qing imperial collections comparative analysis"
```

### 步骤 4: 连接到 GitHub 仓库

添加远程仓库（将 `YOUR_USERNAME` 替换为您的 GitHub 用户名）:

```bash
git remote add origin https://github.com/YOUR_USERNAME/qing-imperial-collections-analysis.git
```

### 步骤 5: 推送到 GitHub

将代码推送到 GitHub:

```bash
git branch -M main
git push -u origin main
```

**注意**: 可能会提示您输入 GitHub 凭据。如果启用了双因素认证，需要使用个人访问令牌（Personal Access Token）代替密码。

### 步骤 6: 验证部署

1. 访问您的仓库 URL: `https://github.com/YOUR_USERNAME/qing-imperial-collections-analysis`
2. 验证所有文件已正确上传
3. 检查 README.md 在仓库主页上是否正确显示

### 可选: 创建 GitHub Pages（用于文档展示）

1. 在 GitHub 上访问您的仓库
2. 点击 **"Settings"**（设置）标签
3. 向下滚动到 **"Pages"**（页面）部分
4. 在 **"Source"**（源）下，选择 **"main"** 分支和 **"/ (root)"**（根目录）文件夹
5. 点击 **"Save"**（保存）
6. 您的文档将在以下地址可用: `https://YOUR_USERNAME.github.io/qing-imperial-collections-analysis/`

### 可选: 添加主题和描述

1. 访问仓库主页
2. 点击 "About" 旁边的齿轮图标 ⚙️
3. 添加主题（标签）:
   - `qing-dynasty`
   - `imperial-collections`
   - `data-visualization`
   - `chinese-art-history`
   - `epigraphy`
   - `python`
   - `matplotlib`
4. 如果创建了 GitHub Pages，添加网站 URL
5. 点击 **"Save changes"**（保存更改）

### 故障排除

#### 认证问题

如果遇到认证问题:

1. **创建个人访问令牌**:
   - 访问 GitHub Settings（设置）→ Developer settings（开发者设置）→ Personal access tokens（个人访问令牌）
   - 点击 "Generate new token"（生成新令牌）
   - 选择权限范围: `repo`（完全控制私有仓库）
   - 复制令牌

2. **推送到 GitHub 时使用令牌作为密码**

#### 大文件问题

如果有超过 100MB 的文件:

1. 使用 Git LFS（大文件存储）:
   ```bash
   git lfs install
   git lfs track "*.png"
   git add .gitattributes
   git commit -m "Add Git LFS tracking"
   ```

---

## Quick Command Reference

### Initial Setup
```bash
cd /home/sandbox/qing-imperial-collections-analysis
git init
git add .
git commit -m "Initial commit: Qing imperial collections comparative analysis"
git remote add origin https://github.com/YOUR_USERNAME/qing-imperial-collections-analysis.git
git branch -M main
git push -u origin main
```

### Subsequent Updates
```bash
git add .
git commit -m "Update: [describe your changes]"
git push
```

### Check Status
```bash
git status
git log
```

---

**Need Help?**
- GitHub Documentation: https://docs.github.com/
- Git Documentation: https://git-scm.com/doc
- GitHub Support: https://support.github.com/

---

**Last Updated**: December 30, 2025
