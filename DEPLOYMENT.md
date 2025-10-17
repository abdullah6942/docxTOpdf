# Deployment Guide for Streamlit Cloud

## 🚀 Quick Deployment Steps

### 1. Prepare Your Repository

Make sure you have these files in your repository root:
- ✅ `convert.py` - Main application
- ✅ `requirements.txt` - Python dependencies
- ✅ `packages.txt` - System packages (LibreOffice)
- ✅ `.gitignore` - To exclude unnecessary files

### 2. Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Add DOCX to PDF converter"

# Add your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### 3. Deploy on Streamlit Cloud

1. **Go to** [share.streamlit.io](https://share.streamlit.io)

2. **Sign in** with your GitHub account

3. **Click** "New app" button

4. **Fill in the details:**
   - **Repository:** Select your GitHub repository
   - **Branch:** `main` (or your default branch)
   - **Main file path:** `convert.py`

5. **Click** "Deploy!"

6. **Wait** for deployment (usually 2-5 minutes)

### 4. Your App is Live! 🎉

Once deployed, you'll get a URL like: `https://your-app-name.streamlit.app`

## 📋 Important Files Explained

### `requirements.txt`
```
streamlit>=1.28.0
```
Contains Python packages needed for your app.

### `packages.txt`
```
libreoffice
```
Contains system-level packages. This tells Streamlit Cloud to install LibreOffice, which is used for DOCX to PDF conversion on Linux servers.

## 🔧 Troubleshooting Deployment

### Error: "No matching distribution found for pywin32"
**Solution:** Remove `pywin32` and `docx2pdf` from `requirements.txt`. The app now uses LibreOffice which works on Linux.

### Error: "LibreOffice command not found"
**Solution:** Make sure `packages.txt` exists and contains `libreoffice`.

### Error: "Module not found"
**Solution:** Check that `requirements.txt` has all necessary packages.

### App crashes during conversion
**Solution:** 
- Check the logs in Streamlit Cloud dashboard
- Ensure the DOCX file is valid
- Try with a smaller file first

## 🔄 Updating Your Deployed App

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update app"
   git push
   ```
3. Streamlit Cloud will **automatically redeploy** your app!

## 🎯 Best Practices

1. **Test Locally First:** Always test your app locally before deploying
2. **Check Logs:** Use the Streamlit Cloud dashboard to view logs
3. **Small Updates:** Make incremental changes for easier debugging
4. **Environment Variables:** Use Streamlit secrets for sensitive data (if needed)

## 📊 Monitoring Your App

- **Dashboard:** [share.streamlit.io/](https://share.streamlit.io/)
- **View logs:** Click on your app → "Manage app" → "Logs"
- **Analytics:** See usage statistics in the dashboard

## 🆓 Free Tier Limits

Streamlit Cloud free tier includes:
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Auto-scaling
- ✅ Custom domains (for private apps)

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Community](https://discuss.streamlit.io/)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)

## ❓ Need Help?

If you encounter issues:
1. Check the Streamlit Cloud logs
2. Visit [Streamlit Community Forum](https://discuss.streamlit.io/)
3. Check the [GitHub Issues](https://github.com/streamlit/streamlit/issues)

---

**Happy Deploying! 🚀**

