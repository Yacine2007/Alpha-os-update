#!/bin/bash

# فحص إذا كانت zenity مثبتة
if command -v zenity >/dev/null 2>&1; then
    zenity --info \
        --title="Alpha OS Update" \
        --text="✅ تم تثبيت التحديث بنجاح!" \
        --width=300 --height=100
else
    echo "Zenity غير مثبت. لا يمكن عرض النافذة."
fi
