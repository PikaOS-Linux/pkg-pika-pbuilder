#! /bin/bash

mkdir -p /etc/apt/sources.list.d

# Clear /etc/apt/sources.list in favor of deb822 formats
tee /etc/apt/sources.list <<'EOF'
## This file is deprecated in PikaOS.
## See /etc/apt/sources.list.d/system.sources.
EOF

# Add Debian Repo
touch /etc/apt/sources.list.d/debian.sources
tee /etc/apt/sources.list.d/debian.sources <<'EOF'
X-Repolib-Name: Debian Sources
Enabled: yes
Types: deb deb-src
URIs: http://deb.debian.org/debian
Suites: sid experimental
Components: main contrib non-free non-free-firmware
X-Repolib-Default-Mirror: http://deb.debian.org/debian
Signed-by: /usr/share/keyrings/debian-archive-keyring.gpg
EOF

# Add Pika Repos
tee /etc/apt/sources.list.d/system.sources <<'EOF'
X-Repolib-Name: PikaOS System Sources
Enabled: yes
Types: deb
URIs: https://ppa.pika-os.com/
Suites: pikauwu
Components: canary
X-Repolib-ID: system
X-Repolib-Default-Mirror: https://ppa.pika-os.com/
Signed-By: /etc/apt/keyrings/pika-keyring.gpg.key
EOF

# Add DMO Repos
tee /etc/apt/sources.list.d/dmo.sources <<'EOF'
X-Repolib-Name: Multimedia Sources
Enabled: yes
Types: deb deb-src
URIs: https://www.deb-multimedia.org
Suites: sid
Components: main non-free
X-Repolib-Default-Mirror: https://www.deb-multimedia.org/
Signed-By: /etc/apt/keyrings/deb-multimedia-keyring.gpg
EOF

# Add Neon Src
tee /etc/apt/sources.list.d/neon.sources <<'EOF'
X-Repolib-Name: KDE Neon Sources
Enabled: yes
Types: deb-src
URIs: http://archive.neon.kde.org/user/
Suites: jammy
Components: main
X-Repolib-Default-Mirror: http://archive.neon.kde.org/user/
Signed-By: /etc/apt/keyrings/kde-neon-keyring.gpg.key
EOF

# Get keyrings
mkdir -p /etc/apt/keyrings/
wget https://github.com/PikaOS-Linux/pika-base-debian-container/raw/main/pika-keyring.gpg.key -O /etc/apt/keyrings/pika-keyring.gpg.key
wget https://github.com/PikaOS-Linux/pika-base-debian-container/raw/main/deb-multimedia-keyring.gpg -O /etc/apt/keyrings/deb-multimedia-keyring.gpg
wget https://github.com/PikaOS-Linux/pika-base-debian-container/raw/main/kde-neon-keyring.gpg.key -O /etc/apt/keyrings/kde-neon-keyring.gpg.key

# Setup apt configration
mkdir -p  /etc/apt/preferences.d/
tee /etc/apt/preferences.d/0-pika-debian-settings <<'EOF'
# Blacklist Packages from being pulled from debian experimental
Package: *libwebrtc-audio-processing*
Pin: release a=experimental
Pin-Priority: 100

Package: *selinux*
Pin: release a=experimental
Pin-Priority: -1

Package: *
Pin: release a=experimental   
Pin-Priority: -1

# Lower Debians's priority under pika's

Package: *
Pin: release o=Debian
Pin-Priority: 400

# We only want gnome from experimental
Package: adwaita-icon-theme at-spi2-core baobab gnome-calls fonts-cantarell d-spy dconf dconf-editor devhelp epiphany-browser evince evolution-data-server folks gcab gcr gcr4 gdk-pixbuf gdm3 geocode-glib gexiv2 gi-docgen gjs glib2.0 glib-networking glibmm2.68 gmime gnome-autoar gnome-backgrounds gnome-bluetooth3 gnome-boxes gnome-builder gnome-calculator gnome-calendar gnome-characters gnome-clocks gnome-color-manager gnome-connections gnome-console gnome-contacts gnome-control-center gnome-desktop gnome-disk-utility gnome-font-viewer gnome-initial-setup gnome-keyring gnome-logs gnome-maps gnome-menus gnome-music gnome-online-accounts gnome-remote-desktop gnome-session gnome-settings-daemon gnome-shell gnome-shell-extensions gnome-software gnome-system-monitor gnome-text-editor gnome-tour gnome-user-docs gnome-user-share gnome-weather gobject-introspection libgom grilo grilo-plugins gsettings-desktop-schemas gsound gspell gssdp gtk4 gtk+3.0 gtk-doc gtk-vnc gtkmm4.0 gtksourceview4 gtksourceview5 gupnp gupnp-av gupnp-dlna gvfs json-glib jsonrpc-glib libadwaita-1 libdazzle libdex libgee-0.8 libgsf libgtop2 libgweather4 libgxps libhandy-1 libmediaart libnma libnotify libpanel libpeas libpeas2 librsvg libsecret libshumate libsigc++-3.0 libsoup3 loupe mm-common mutter nautilus orca pango1.0 pangomm2.48 phodav pyatspi pygobject librest rygel simple-scan gnome-snapshot gnome-sushi sysprof tecla template-glib totem totem-pl-parser tracker tracker-miners vala vte2.91 xdg-desktop-portal-gnome yelp yelp-tools yelp-xsl telepathy-farstream telepathy-glib telepathy-haze telepathy-idle telepathy-mission-control-5 telepathy-qt telepathy-rakia telepathy-spec
Pin: release a=experimental   
Pin-Priority: 425

Package: *
Pin: release o=Unofficial Multimedia Packages
Pin-Priority: 450

# Neon blacklist
Package: neon-desktop base-files
Pin: origin archive.neon.kde.org
Pin-Priority: -1

# Give pika lowest priority because we don't want it sources overwriting
Package: *
Pin: release a=pikauwu,c=canary
Pin-Priority: 390
EOF

tee /etc/apt/preferences.d/1-pika-radeon-settings <<'EOF'
Package: libhsa-runtime64*
Pin: release o=Debian
Pin-Priority: 100

Package: hipcc*
Pin: release o=Debian
Pin-Priority: 100

Package: rocm*
Pin: release o=Debian
Pin-Priority: 100

Package: *
Pin: release c=rocm
Pin-Priority: 400

Package: amdgpu-core amdgpu-pro-core amdgpu-dkms amdgpu-pro-lib32
Pin: release a=*
Pin-Priority: -10
EOF
