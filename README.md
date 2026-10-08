# Yashica M — AI & Data Science Engineer Portfolio

> A high-performance, single-page portfolio engineered for **Yashica M**, a final-year B.Tech Artificial Intelligence & Data Science (Honors) student seeking entry-level **AI/ML**, **Software Developer**, or **Data** roles at MNCs and through campus placements.

---

## 🚀 Live Highlights & Features

- **⚡ Zero-Build Overhead**: Built with pure semantic HTML5, modern CSS3 design tokens, and modular ES6 JavaScript. Instantaneous First Contentful Paint (FCP) and 100 Lighthouse performance.
- **🎨 Modern Recruiter-Friendly Aesthetics**:
  - Deep Navy background (`#0A0E1A`) with electric indigo (`#6366F1`), violet (`#8B5CF6`), and cyber cyan (`#06B6D4`) accents.
  - Sleek Light Mode toggle with automatic system preference detection and `localStorage` persistence.
  - Glassmorphic card surfaces, subtle ambient background glows, and micro-interactions.
- **🧭 Dynamic Navigation & Scroll Spy**: Sticky glassmorphism header that automatically highlights the active section as you scroll.
- **🏷️ Interactive Project Filtering**: Instant category switching across **All Projects**, **AI / ML**, and **Full-Stack** with animated transitions.
- **📊 Animated Stats Counters**: IntersectionObserver-powered counter animation for key academic and research statistics.
- **📋 One-Click Email Copy**: Clickable copy action with feedback toast notification (`yashica586@gmail.com`).
- **📄 Downloadable PDF Resume**: Integrated `resume.pdf` with complete academic and research details ready for ATS and recruiter review.
- **♿ Accessible & SEO-Optimized**: Full keyboard navigation (`:focus-visible`), skip-to-content link, semantic landmarks, Open Graph cards, Twitter cards, and Schema.org JSON-LD structured data.

---

## 📁 Repository Structure

```text
portfolio/
├── index.html               # Semantic single-page structure, SEO & Open Graph meta tags
├── styles.css               # Design tokens, CSS variables, dark/light themes, animations
├── script.js                # Theme toggle, scroll-spy, filters, stats counters, toasts
├── resume.pdf               # Professional 1-page ATS-formatted PDF resume
├── generate_resume.py       # Python ReportLab generator to update resume.pdf anytime
├── README.md                # Deployment and project documentation
└── assets/
    ├── favicon.svg          # Modern neural spark SVG favicon
    └── images/
        ├── yashica-portrait.jpg    # Professional studio portrait headshot
        ├── project-ainewus.jpg     # AI Newus platform dashboard visual
        ├── project-cvinsight.jpg   # CVInsightAI resume analyzer screenshot
        └── project-fashionmnist.jpg # Fashion-MNIST CNN deep vision experiment visual
```

---

## 💻 Local Development & Preview

Because this project uses vanilla web standards, no `npm install` or compilation step is required.

### Option 1: Python HTTP Server (Recommended)
```bash
# In the portfolio directory:
python -m http.server 3000
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### Option 2: Node.js (npx serve)
```bash
npx serve .
```

### Option 3: VS Code / IDE Live Server
Right-click `index.html` and click **"Open with Live Server"**.

---

## 🌐 Deployment Instructions

### 1. GitHub Pages (Free & Instant)

1. Initialize git and commit files:
   ```bash
   git init
   git add .
   git commit -m "feat: initial release of Yashica M portfolio"
   ```
2. Create a new GitHub repository named `portfolio` under your GitHub account (`yashica-tech-flare`).
3. Push your code:
   ```bash
   git branch -M main
   git remote add origin https://github.com/yashica-tech-flare/portfolio.git
   git push -u origin main
   ```
4. On GitHub, go to **Settings** → **Pages** → under **Build and deployment**, select:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` / `/ (root)`
5. Click **Save**. Your site will be live at:
   `https://yashica-tech-flare.github.io/portfolio/`

---

### 2. Vercel

#### Method A: Via Vercel Dashboard
1. Go to [vercel.com](https://vercel.com) and log in with your GitHub account.
2. Click **"Add New Project"** → Import your `portfolio` repository.
3. Keep default settings (Framework Preset: **Other**, Root Directory: `./`).
4. Click **Deploy**. Your portfolio is instantly live on a custom `*.vercel.app` domain.

#### Method B: Via Vercel CLI
```bash
npm i -g vercel
vercel
```

---

### 3. Netlify

#### Method A: Drag and Drop (No Git required)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop the `portfolio` folder directly into the upload area.
3. Your site deploys in seconds.

#### Method B: Git Integration
1. Connect your GitHub repository to Netlify.
2. Leave Build Command blank, set Publish Directory to `./`.
3. Click **Deploy Site**.

---

## 🛠️ Updating the Resume PDF

If you update your CGPA, add new certifications, or publish new research papers:
1. Open `generate_resume.py`.
2. Update the details in the script.
3. Run:
   ```bash
   python generate_resume.py
   ```
4. A fresh `resume.pdf` will be compiled and linked directly to the **"Download Resume"** button on the website!

---

## 📬 Contact & Credentials

- **Engineer**: Yashica M
- **Role**: AI & Data Science Engineer (Honors)
- **Institution**: K.L.N. College of Engineering (Affiliated to Anna University)
- **Email**: [yashica586@gmail.com](mailto:yashica586@gmail.com)
- **LinkedIn**: [linkedin.com/in/yashica-m-586-leadingstar](https://www.linkedin.com/in/yashica-m-586-leadingstar)
- **GitHub**: [github.com/yashica-tech-flare](https://github.com/yashica-tech-flare)
