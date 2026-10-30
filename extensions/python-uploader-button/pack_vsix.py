import json
import zipfile
from pathlib import Path

ext = Path(__file__).resolve().parent
pkg = json.loads((ext / "package.json").read_text(encoding="utf-8"))
name = pkg["name"]
ver = pkg["version"]
pub = pkg.get("publisher", "mbot2-club")
vsix = ext / f"{pub}-{name}-{ver}.vsix"

manifest = f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="{name}" Version="{ver}" Publisher="{pub}" />
    <DisplayName>{pkg.get("displayName", name)}</DisplayName>
    <Description xml:space="preserve">{pkg.get("description", "")}</Description>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
  </Assets>
</PackageManifest>
"""

ctypes = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension=".json" ContentType="application/json"/>
  <Default Extension=".js" ContentType="application/javascript"/>
  <Default Extension=".md" ContentType="text/markdown"/>
  <Default Extension=".vsixmanifest" ContentType="text/xml"/>
</Types>
"""

with zipfile.ZipFile(vsix, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("extension.vsixmanifest", manifest)
    zf.writestr("[Content_Types].xml", ctypes)
    for fname in ("package.json", "extension.js", "README.md"):
        zf.write(ext / fname, f"extension/{fname}")

print(vsix)
