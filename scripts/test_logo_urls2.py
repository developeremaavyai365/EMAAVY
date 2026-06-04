import urllib.request

urls = [
    "https://cdn.worldvectorlogo.com/logos/plivo.svg",
    "https://cdn.worldvectorlogo.com/logos/plivo-1.svg",
    "https://cdn.worldvectorlogo.com/logos/plivo-2.svg",
    "https://cdn.worldvectorlogo.com/logos/telnyx.svg",
    "https://cdn.worldvectorlogo.com/logos/telnyx-1.svg",
    "https://cdn.worldvectorlogo.com/logos/telnyx-2.svg",
    "https://cdn.worldvectorlogo.com/logos/plivo-inc.svg",
    "https://cdn.worldvectorlogo.com/logos/plivo-logo.svg",
    "https://companieslogo.com/img/orig/PLVO_BIG-ICON.png",
    "https://www.google.com/s2/favicons?domain=plivo.com&sz=128",
    "https://www.google.com/s2/favicons?domain=telnyx.com&sz=128",
    "https://logo.dev/plivo.com?token=pk_X",
]

ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
for u in urls:
    try:
        req = urllib.request.Request(u, headers=ua)
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
            print("OK", r.status, len(data), r.headers.get("content-type", ""), u)
    except Exception as e:
        print("FAIL", u, "-", e)
