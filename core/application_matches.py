from talon import Module

mod = Module()


apps = mod.apps

# apple specific apps
apps.datagrip = """
os: mac
and app.name: DataGrip
"""

apps.finder = """
os: mac
and app.bundle: com.apple.finder
"""

apps.rstudio = """
os: mac
and app.name: RStudio
"""

apps.apple_terminal = """
os: mac
and app.bundle: com.apple.Terminal
"""

# linux specific apps
apps.keepass = """
os: linux
and app.name: KeePassX2
os: linux
and app.name: KeePassXC
os: linux
and app.name: KeepassX2
os: linux
and app.name: keepassx2
os: linux
and app.name: keepassxc
os: linux
and app.name: Keepassxc"""

apps.signal = """
os: linux
and app.name: Signal

os: linux
and app.name: signal

os: linux
and app.name: Signal-desktop

"""

apps.zathura = """
os: linux
and app.name: Zathura

os: linux
and app.name: zathura

"""

apps.termite = """
os: linux
and app.name: /termite/
"""

apps.kitty = """
os: linux
and app.name: /kitty/
"""

apps.windows_explorer = """
os: windows
and app.name: Windows Explorer
os: windows
and app.exe: explorer.exe
"""

apps.windows_command_processor = """
os: windows
and app.name: Windows Command Processor
os: windows
and app.exe: cmd.exe
"""

apps.windows_terminal = """
os: windows
and app.exe: WindowsTerminal.exe
"""


apps.vim = """
app.name:neovide
"""

apps.vim = """
win.title:/VIM/
"""

apps.vmware = """
app.name: vmware
app.name: Vmware
"""

apps.libreoffice_writer = """
app.name: LibreOffice Writer
"""

apps.stellaris = """
app.name: stellaris
"""

# O10editor because we can't lead with a 0
apps.O10editor = """
app.name: 010editor
app.name: 010 Editor
"""

apps.openshot = """
os: linux
and app.name: openshot-qt

os: linux
and app.name: openshot

win.title:/OpenShot Video Editor/
"""

apps.sqlitebrowser = """
os: linux
and app.name: "/DB Browser for SQLite/"
"""

apps.windows_power_shell = """
os: windows
and app.exe: powershell.exe
"""

apps.remmina = """
os: linux
and app.name: "/Remmina/"
"""

apps.drawio = """
os: linux
and app.name: "draw.io"
"""

apps.ida = """
os: linux
and app.name: IDA
"""

apps.hexrays_vault = """
win.title:/IDA Teams/
"""

apps.microsoft_teams = """
os: linux
and app.name: Teams
"""

apps.gnome_terminal = """
os: linux
and app.name: kgx
"""

apps.arandr = """
os: linux
and app.name: arandr
os: linux
and app.name: Arandr
"""

apps.virtualbox_manager = """
os: linux
and win.title:Oracle VM VirtualBox Manager
"""

apps.virtualbox = """
os: linux
and app.name: VirtualBox
"""

apps.openvpn_connect = """
os: mac
and app.bundle: org.openvpn.client.app
"""

apps.copyq = """
os: linux
and win.title: /CopyQ/
"""

apps.utm = """
os: mac
and app.bundle: com.utmapp.UTM
"""

apps.terminal = """
app: zsh
app: wezterm
app: kitty
app: gnome-terminal
app: termite
app: alacritty
"""

apps.wezterm = """
app.name: /wezterm/
"""

apps.alacritty = """
app.name: /alacritty/
"""
