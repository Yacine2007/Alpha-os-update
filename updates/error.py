import subprocess
import os

def run_alpha_command(command):
    print(f"--- Alpha OS Terminal: Executing '{command}' ---")
    try:
        # تنفيذ الأمر والانتظار حتى ينتهي
        # shell=True تسمح بتشغيل الأوامر مباشرة كأنك في CMD
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        
        # عرض مخرجات الأمر إذا نجح
        print("Output:\n", result.stdout)
        
    except subprocess.CalledProcessError as e:
        # في حال فشل الأمر (وهو المتوقع مع ErrorTest) سيظهر الخطأ هنا
        print(f"System Alert: Command failed with error.")
        print(f"Error Log:\n{e.stderr}")

# تنفيذ أمر ErrorTest مباشرة
if __name__ == "__main__":
    run_alpha_command("Errortest")
