#!/bin/bash

# فقط root
if [ "$EUID" -ne 0 ]; then
  echo "يرجى تشغيل السكربت كـ root: sudo ./install-alphaos.sh"
  exit 1
fi

packages=(
  kde-gtk-config
  mpv
  gthumb
  thunar
  xarchiver
  clipit
  qpdfview
  mousepad
  xfce4-notes
)

logfile="/tmp/alphaos-install.log"
echo "بدأ التثبيت: $(date)" > "$logfile"

for pkg in "${packages[@]}"; do
  echo "تثبيت ↦ $pkg ..." | tee -a "$logfile"
  if apt-get install -y "$pkg" >> "$logfile" 2>&1; then
    echo "✅ تمّ تثبيت $pkg" | tee -a "$logfile"
  else
    echo "⚠️ فشل تثبيت $pkg" | tee -a "$logfile"
  fi
done

echo "انتهاء التثبيت: $(date)" >> "$logfile"

# عرض النتائج في نافذة ترمنال جديدة
x-terminal-emulator -e bash -c "echo 'نتائج التثبيت:'; cat '$logfile'; echo ''; echo 'اضغط Enter للإغلاق'; read"
