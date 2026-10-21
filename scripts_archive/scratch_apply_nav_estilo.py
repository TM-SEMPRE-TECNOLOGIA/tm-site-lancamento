import re

css_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\css\estilo.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

navbar_global_css = """
/* =========================================================
   GLOBAL BULLETPROOF NAVBAR FIX (SOLID BG, NO-WRAP, CRISP LOGO)
   ========================================================= */
.navbar, .navbar.white-style {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  width: 100% !important;
  height: 76px !important;
  background-color: rgba(255, 255, 255, 0.98) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  box-shadow: 0 2px 14px rgba(0, 0, 0, 0.07) !important;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06) !important;
  z-index: 9999 !important;
  padding: 0 20px !important;
  display: flex !important;
  align-items: center !important;
  box-sizing: border-box !important;
}

.navbar .container.w-container {
  max-width: 1440px !important;
  width: 100% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  height: 100% !important;
  margin: 0 auto !important;
  padding: 0 !important;
}

.navbar .brand {
  height: 48px !important;
  display: flex !important;
  align-items: center !important;
  flex-shrink: 0 !important;
  margin: 0 16px 0 0 !important;
  padding: 0 !important;
}

.navbar .brand img.logo-image {
  max-height: 42px !important;
  width: auto !important;
  display: block !important;
  object-fit: contain !important;
}

.navbar .nav-menu {
  display: flex !important;
  align-items: center !important;
  flex-wrap: nowrap !important;
  height: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  gap: 2px !important;
}

.navbar .navlink {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 6px 9px !important;
  white-space: nowrap !important;
  text-decoration: none !important;
  border-bottom: none !important;
  transition: all 0.2s ease !important;
}

.navbar .navlink .nav-text {
  color: #102234 !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  white-space: nowrap !important;
  line-height: 1.2 !important;
  letter-spacing: -0.2px !important;
  transition: color 0.2s ease !important;
}

.navbar .navlink:hover .nav-text {
  color: #FFBE00 !important;
}

.navbar .navlink.media {
  padding: 6px 6px !important;
  margin-left: 4px !important;
}

.navbar .navlink.media img {
  width: 24px !important;
  height: 24px !important;
  display: block !important;
}

@media (max-width: 1200px) {
  .navbar .navlink {
    padding: 5px 6px !important;
  }
  .navbar .navlink .nav-text {
    font-size: 12.5px !important;
  }
}

@media (max-width: 991px) {
  .navbar .nav-menu {
    background-color: #ffffff !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1) !important;
    padding: 16px 20px !important;
  }
  .navbar .navlink {
    padding: 10px 14px !important;
    border-bottom: 1px solid #f1f5f9 !important;
    width: 100% !important;
    justify-content: flex-start !important;
  }
  .navbar .navlink .nav-text {
    font-size: 15px !important;
  }
}
"""

if 'GLOBAL BULLETPROOF NAVBAR FIX' not in css:
    css = css + '\n' + navbar_global_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Appended navbar fix to estilo.css!")
else:
    print("Navbar fix already in estilo.css")
