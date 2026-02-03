#!/bin/bash

# ألوان للتنسيق
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# مسح الشاشة
clear

# عرض عنوان النظام
echo -e "${CYAN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║               █████  ██      ██████  ██   ██ █████       ║"
echo "║              ██   ██ ██      ██   ██ ██   ██ ██   ██     ║"
echo "║              ███████ ██      ██████  ███████ ██████      ║"
echo "║              ██   ██ ██      ██   ██ ██   ██ ██   ██     ║"
echo "║              ██   ██ ███████ ██████  ██   ██ ██   ██     ║"
echo "║                                                          ║"
echo "║                  A L P H A   O S                         ║"
echo "║                  Version 26.3 (Dolphin)                  ║"
echo "║                Debian-based Distribution                 ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╗"
echo -e "${NC}"

# رسالة ترحيب
echo -e "${YELLOW}${BOLD}"
echo "════════════════════════════════════════════════════════════"
echo "              WELCOME TO ALPHA OS v26.3"
echo "════════════════════════════════════════════════════════════"
echo -e "${NC}"

# عرض معلومات النظام
echo -e "${WHITE}${BOLD}"
echo "┌──────────────────────────────────────────────────────────┐"
echo "│                     SYSTEM INFORMATION                   │"
echo "├──────────────────────────────────────────────────────────┤"
echo -e "${NC}"

# اسم المستخدم والنظام
echo -e "${CYAN}User:${NC} ${WHITE}$(whoami)${NC}"
echo -e "${CYAN}Hostname:${NC} ${WHITE}$(hostname)${NC}"
echo -e "${CYAN}System:${NC} ${WHITE}Alpha OS v26.3${NC}"
echo -e "${CYAN}Kernel:${NC} ${WHITE}$(uname -r)${NC}"
echo -e "${CYAN}Uptime:${NC} ${WHITE}$(uptime -p | sed 's/up //')${NC}"

# فحص وتحديثات النظام
echo -e "\n${WHITE}${BOLD}"
echo "┌──────────────────────────────────────────────────────────┐"
echo "│                SYSTEM UPDATES CHECK                      │"
echo "├──────────────────────────────────────────────────────────┤"
echo -e "${NC}"

# محاكاة فحص التحديثات
echo -e "${YELLOW}Checking for system updates...${NC}"
sleep 2

# محاكاة تحديثات ناجحة
echo -e "${GREEN}${BOLD}"
echo "✓ All packages are up to date!"
echo "✓ System security patches: Applied"
echo "✓ Software repositories: Synchronized"
echo "✓ Kernel updates: Available (stable)"
echo -e "${NC}"

# رسالة نجاح التحديثات
echo -e "\n${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}         SYSTEM UPDATE STATUS: SUCCESSFUL!              ${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"

# نص الاختبار
echo -e "\n${MAGENTA}${BOLD}"
echo "┌──────────────────────────────────────────────────────────┐"
echo "│                       TEST MESSAGE                       │"
echo "├──────────────────────────────────────────────────────────┤"
echo "│ This is a test message showing the terminal colors      │"
echo "│ and formatting capabilities in Alpha OS v26.3.          │"
echo "│                                                          │"
echo "│ ✅  Test 1: Color display - PASSED                      │"
echo "│ ✅  Test 2: System information - PASSED                 │"
echo "│ ✅  Test 3: Update status - PASSED                      │"
echo "│ ✅  Test 4: Welcome message - PASSED                    │"
echo "└──────────────────────────────────────────────────────────┘"
echo -e "${NC}"

# معلومات مفيدة
echo -e "\n${BLUE}${BOLD}"
echo "════════════════════════════════════════════════════════════"
echo "                 QUICK COMMANDS REFERENCE"
echo "════════════════════════════════════════════════════════════"
echo -e "${NC}"
echo -e "${WHITE}• ${CYAN}update-system${NC}: Update your system packages"
echo -e "${WHITE}• ${CYAN}alpha-info${NC}: Show detailed system information"
echo -e "${WHITE}• ${CYAN}alpha-support${NC}: Get support for Alpha OS"
echo -e "${WHITE}• ${CYAN}check-updates${NC}: Check for available updates"
echo -e "${WHITE}• ${CYAN}restart-services${NC}: Restart system services"

# تحذير أخير
echo -e "\n${YELLOW}${BOLD}⚠  Important:${NC}${YELLOW} Always backup your data before major updates.${NC}"

# رسالة ختامية
echo -e "\n${GREEN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║        Alpha OS v26.3 is ready for use!                 ║"
echo "║        Enjoy your experience with our distribution.      ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# معلومات الإصدار
echo -e "${WHITE}Last checked: $(date)${NC}"
echo -e "${WHITE}Session started at: $(date '+%H:%M:%S')${NC}"