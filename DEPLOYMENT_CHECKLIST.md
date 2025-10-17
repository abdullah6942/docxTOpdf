# ✅ Deployment Checklist for Streamlit Cloud

Use this checklist to ensure your app is ready for deployment.

## 📋 Pre-Deployment Checklist

### Required Files
- [ ] `convert.py` exists and is updated
- [ ] `requirements.txt` exists (only has `streamlit>=1.28.0`)
- [ ] `packages.txt` exists (has `libreoffice`)
- [ ] `.gitignore` exists (excludes `decx_env/`)

### Git Setup
- [ ] Git repository initialized (`git init`)
- [ ] All files added (`git add .`)
- [ ] Changes committed (`git commit -m "message"`)
- [ ] GitHub repository created
- [ ] Remote added (`git remote add origin <url>`)
- [ ] Code pushed to GitHub (`git push -u origin main`)

### Code Verification
- [ ] App runs locally without errors
- [ ] Test file upload works
- [ ] Test conversion works
- [ ] Test download works
- [ ] No hardcoded paths or secrets

## 🚀 Deployment Steps

1. [ ] Go to [share.streamlit.io](https://share.streamlit.io)
2. [ ] Sign in with GitHub
3. [ ] Click "New app"
4. [ ] Select repository: `YOUR_USERNAME/YOUR_REPO`
5. [ ] Select branch: `main`
6. [ ] Set main file: `convert.py`
7. [ ] Click "Deploy!"
8. [ ] Wait for deployment (2-5 minutes)

## ✅ Post-Deployment Checks

- [ ] App loads without errors
- [ ] Upload button works
- [ ] Can upload a DOCX file
- [ ] Conversion completes successfully
- [ ] Download button appears
- [ ] PDF downloads correctly
- [ ] Check logs for any warnings

## 🔍 Troubleshooting

If deployment fails, check:

- [ ] `packages.txt` is in repository root
- [ ] No Windows-specific packages in `requirements.txt`
- [ ] File names are correct (case-sensitive)
- [ ] All files are pushed to GitHub
- [ ] Check Streamlit Cloud logs for errors

## 📱 Share Your App

Once deployed:
- [ ] Copy your app URL: `https://your-app-name.streamlit.app`
- [ ] Test from different devices
- [ ] Share with users

## 🎉 Success!

Your DOCX to PDF converter is now live!

---

**Need help?** Check `DEPLOYMENT.md` for detailed instructions.

