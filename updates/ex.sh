#!/bin/bash

# فتح lxterminal وعرض الرسالة
if command -v lxterminal >/dev/null 2>&1; then
    lxterminal -e bash -c 'echo "The update was successfully installed."; read -n 1 -s -r -p "اضغط أي مفتاح لإغلاق التحديث..."'
else
    echo "lxterminal غير موجود في النظام."
fi
