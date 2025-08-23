import time
import os
import sys
from colorama import init, Fore, Back, Style

# تهيئة colorama للتعامل مع الألوان في الطرفية
init(autoreset=True)

def clear_screen():
    """مسح الشاشة"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text):
    """طباعة نص في مركز الشاشة"""
    width = os.get_terminal_size().columns
    print(text.center(width))

def print_success_banner():
    """طباعة بانر نجاح مُميز"""
    clear_screen()
    
    # ألوان متناسقة
    colors = [Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE]
    
    # تصميم البانر
    banner = [
        "╔══════════════════════════════════════════════════════════════╗",
        "║                                                              ║",
        "║  ███╗   ██╗ ██████╗ ███████╗    ███████╗ █████╗  ██████╗     ║",
        "║  ████╗  ██║██╔════╝ ██╔════╝    ██╔════╝██╔══██╗██╔════╝     ║",
        "║  ██╔██╗ ██║██║  ███╗███████╗    ███████╗███████║██║  ███╗    ║",
        "║  ██║╚██╗██║██║   ██║╚════██║    ╚════██║██╔══██║██║   ██║    ║",
        "║  ██║ ╚████║╚██████╔╝███████║    ███████║██║  ██║╚██████╔╝    ║",
        "║  ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝     ║",
        "║                                                              ║",
        "╚══════════════════════════════════════════════════════════════╝"
    ]
    
    # عرض البانر مع تأثيرات الألوان
    for i, line in enumerate(banner):
        color = colors[i % len(colors)]
        print_centered(color + line)
        time.sleep(0.1)
    
    time.sleep(0.5)
    
    # رسائل التهنئة
    messages = [
        "",
        "🎉 مبروك! لقد نجحت في الاختبار 🎉",
        "",
        "✨ لقد أظهرت تميزاً رائعاً ومهارة استثنائية ✨",
        "",
        "🏆 هذا الإنجاز يستحق الاحتفاء به 🏆",
        ""
    ]
    
    for msg in messages:
        print_centered(Fore.YELLOW + Style.BRIGHT + msg)
        time.sleep(0.3)
    
    time.sleep(1)
    
    # معلومات إضافية
    details = [
        "",
        f"{Fore.GREEN}➤ تاريخ الإنجاز: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"{Fore.CYAN}➤ مستوى الأداء: ممتاز",
        f"{Fore.MAGENTA}➤ النتيجة: 100%",
        ""
    ]
    
    for detail in details:
        print_centered(detail)
        time.sleep(0.2)
    
    time.sleep(1)
    
    # تأثيرات نهائية
    print_centered(Fore.WHITE + Back.GREEN + "=" * 60)
    print_centered(Fore.BLACK + Back.YELLOW + " 🎓 تهانينا الحارة على هذا الإنجاز الكبير! 🎓 ")
    print_centered(Fore.WHITE + Back.GREEN + "=" * 60)
    
    time.sleep(2)
    
    # رسالة تشجيعية نهائية
    encouragement = [
        "",
        f"{Fore.CYAN}استمر في التميز والعطاء، فالعالم يحتاج إلى مواهبك!",
        f"{Fore.GREEN}هذا هو فقط بداية طريق النجاح...",
        ""
    ]
    
    for line in encouragement:
        print_centered(line)
        time.sleep(0.5)

def animate_confetti():
    """إضافة تأثير كونفيتي متحرك"""
    confetti_chars = ["✨", "🎉", "🎊", "🎈", "⭐", "🌟", "💫", "🎯", "🏆", "🎓"]
    
    print("\n\n")
    for _ in range(5):
        line = " ".join([confetti_chars[i % len(confetti_chars)] for i in range(20))
        print_centered(Fore.YELLOW + line)
        time.sleep(0.3)
    
    print("\n")

def main():
    """الدالة الرئيسية"""
    try:
        print_success_banner()
        animate_confetti()
        
        # بقاء الشاشة معطلة حتى الضغط على زر
        print_centered(Fore.WHITE + Back.BLUE + "اضغط على أي مفتاح للمتابعة...")
        if os.name == 'nt':
            import msvcrt
            msvcrt.getch()
        else:
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    main()
