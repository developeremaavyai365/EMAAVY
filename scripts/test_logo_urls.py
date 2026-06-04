import urllib.request

urls = [
    "https://cdn.worldvectorlogo.com/logos/plivo.svg",
    "https://cdn.worldvectorlogo.com/logos/plivo-1.svg",
    "https://cdn.worldvectorlogo.com/logos/telnyx.svg",
    "https://cdn.worldvectorlogo.com/logos/telnyx-1.svg",
    "https://www.plivo.com/wp-content/themes/plivo/assets/images/logo.svg",
    "https://telnyx.com/favicon.svg",
    "https://companieslogo.com/img/orig/TELNYX_BIG-ICON.png",
    "https://upload.wikimedia.org/wikipedia/commons/8/8a/Plivo_logo.svg",
    "https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/svg/plivo.svg",
    "https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/svg/telnyx.svg",
    "https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/plivo.svg",
    "https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/telnyx.svg",
]

for u in urls:
    try:
        req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            print(r.status, r.headers.get("content-type", ""), u)
    except Exception as e:
        print("FAIL", u, "-", e)
