import telebot
import os
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# API Token
API_TOKEN = '8595567289:AAGtlACEklFZjZkfK7cvVJo9HIosz5Gz7t8'
bot = telebot.TeleBot(API_TOKEN)

# Download Path
DOWNLOAD_PATH = '/storage/emulated/0/Download/'

# --- FULL DATABASE (120+ All Country Flags & Codes) ---
COUNTRY_DB = {
    "Afghanistan": ("🇦🇫", "+93"), "Albania": ("🇦🇱", "+355"), "Algeria": ("🇩🇿", "+213"), "Andorra": ("🇦🇩", "+376"),
    "Angola": ("🇦🇴", "+244"), "Argentina": ("🇦🇷", "+54"), "Armenia": ("🇦🇲", "+374"), "Australia": ("🇦🇺", "+61"),
    "Austria": ("🇦🇹", "+43"), "Azerbaijan": ("🇦🇿", "+994"), "Bahrain": ("🇧🇭", "+973"), "Bangladesh": ("🇧🇩", "+880"),
    "Belarus": ("🇧🇾", "+375"), "Belgium": ("🇧🇪", "+32"), "Benin": ("🇧🇯", "+229"), "Bhutan": ("🇧🇹", "+975"),
    "Bolivia": ("🇧🇴", "+591"), "Bosnia": ("🇧🇦", "+387"), "Botswana": ("🇧🇼", "+267"), "Brazil": ("🇧🇷", "+55"),
    "Brunei": ("🇧🇳", "+673"), "Bulgaria": ("🇧🇬", "+359"), "Burkina Faso": ("🇧🇫", "+226"), "Burundi": ("🇧🇮", "+257"),
    "Cambodia": ("🇰🇭", "+855"), "Cameroon": ("🇨🇲", "+237"), "Canada": ("🇨🇦", "+1"), "Chad": ("🇹🇩", "+235"),
    "Chile": ("🇨🇱", "+56"), "China": ("🇨🇳", "+86"), "Colombia": ("🇨🇴", "+57"), "Congo": ("🇨🇬", "+242"),
    "Costa Rica": ("🇨🇷", "+506"), "Croatia": ("🇭🇷", "+385"), "Cuba": ("🇨🇺", "+53"), "Cyprus": ("🇨🇾", "+357"),
    "Czech Republic": ("🇨🇿", "+420"), "Denmark": ("🇩🇰", "+45"), "Djibouti": ("🇩🇯", "+253"), "Dominica": ("🇩🇲", "+1"),
    "Ecuador": ("🇪🇨", "+593"), "Egypt": ("🇪🇬", "+20"), "El Salvador": ("🇸🇻", "+503"), "Estonia": ("🇪🇪", "+372"),
    "Ethiopia": ("🇪🇹", "+251"), "Fiji": ("🇫🇯", "+679"), "Finland": ("🇫🇮", "+358"), "France": ("🇫🇷", "+33"),
    "Gabon": ("🇬🇦", "+241"), "Gambia": ("🇬🇲", "+220"), "Georgia": ("🇬🇪", "+995"), "Germany": ("🇩🇪", "+49"),
    "Ghana": ("🇬🇭", "+233"), "Greece": ("🇬🇷", "+30"), "Guatemala": ("🇬🇹", "+502"), "Guinea": ("🇬🇳", "+224"),
    "Guyana": ("🇬🇾", "+592"), "Haiti": ("🇭🇹", "+509"), "Honduras": ("🇭🇳", "+504"), "Hungary": ("🇭🇺", "+36"),
    "Iceland": ("🇮🇸", "+354"), "India": ("🇮🇳", "+91"), "Indonesia": ("🇮🇩", "+62"), "Iran": ("🇮🇷", "+98"),
    "Iraq": ("🇮🇶", "+964"), "Ireland": ("🇮🇪", "+353"), "Israel": ("🇮🇱", "+972"), "Italy": ("🇮🇹", "+39"),
    "Jamaica": ("🇯🇲", "+1"), "Japan": ("🇯🇵", "+81"), "Jordan": ("🇯🇴", "+962"), "Kazakhstan": ("🇰🇿", "+7"),
    "Kenya": ("🇰🇪", "+254"), "Kuwait": ("🇰🇼", "+965"), "Kyrgyzstan": ("🇰🇬", "+996"), "Laos": ("🇱🇦", "+856"),
    "Latvia": ("🇱🇻", "+371"), "Lebanon": ("🇱🇧", "+961"), "Libya": ("🇱🇾", "+218"), "Lithuania": ("🇱🇹", "+370"),
    "Luxembourg": ("🇱🇺", "+352"), "Madagascar": ("🇲🇬", "+261"), "Malaysia": ("🇲🇾", "+60"), "Maldives": ("🇲🇻", "+960"),
    "Mali": ("🇲🇱", "+223"), "Malta": ("🇲🇹", "+356"), "Mauritania": ("🇲🇷", "+222"), "Mauritius": ("🇲🇺", "+230"),
    "Mexico": ("🇲🇽", "+52"), "Moldova": ("🇲🇩", "+373"), "Monaco": ("🇲🇨", "+377"), "Mongolia": ("🇲🇳", "+976"),
    "Morocco": ("🇲🇦", "+212"), "Myanmar": ("🇲🇲", "+95"), "Namibia": ("🇳🇦", "+264"), "Nepal": ("🇳🇵", "+977"),
    "Netherlands": ("🇳🇱", "+31"), "New Zealand": ("🇳🇿", "+64"), "Nicaragua": ("🇳🇮", "+505"), "Niger": ("🇳🇪", "+227"),
    "Nigeria": ("🇳🇬", "+234"), "Norway": ("🇳🇴", "+47"), "Oman": ("🇴🇲", "+968"), "Pakistan": ("🇵🇰", "+92"),
    "Panama": ("🇵🇦", "+507"), "Paraguay": ("🇵🇾", "+595"), "Peru": ("🇵🇪", "+51"), "Philippines": ("🇵🇭", "+63"),
    "Poland": ("🇵🇱", "+48"), "Portugal": ("🇵🇹", "+351"), "Qatar": ("🇶🇦", "+974"), "Romania": ("🇷🇴", "+40"),
    "Russia": ("🇷🇺", "+7"), "Rwanda": ("🇷🇼", "+250"), "Saudi Arabia": ("🇸🇦", "+966"), "Senegal": ("🇸🇳", "+221"),
    "Serbia": ("🇷🇸", "+381"), "Singapore": ("🇸🇬", "+65"), "Slovakia": ("🇸🇰", "+421"), "Slovenia": ("🇸🇮", "+386"),
    "South Africa": ("🇿🇦", "+27"), "South Korea": ("🇰🇷", "+82"), "Spain": ("🇪🇸", "+34"), "Sri Lanka": ("🇱🇰", "+94"),
    "Sudan": ("🇸🇩", "+249"), "Sweden": ("🇸🇪", "+46"), "Switzerland": ("🇨🇭", "+41"), "Syria": ("🇸🇾", "+963"),
    "Taiwan": ("🇹🇼", "+886"), "Tajikistan": ("🇹🇯", "+992"), "Tanzania": ("🇹🇿", "+255"), "Thailand": ("🇹🇭", "+66"),
    "Tunisia": ("🇹🇳", "+216"), "Turkey": ("🇹🇷", "+90"), "Turkmenistan": ("🇹🇲", "+993"), "Uganda": ("🇺🇬", "+256"),
    "Ukraine": ("🇺🇦", "+380"), "UAE": ("🇦🇪", "+971"), "UK": ("🇬🇧", "+44"), "USA": ("🇺🇸", "+1"),
    "Uruguay": ("🇺🇾", "+598"), "Uzbekistan": ("🇺🇿", "+998"), "Vatican City": ("🇻🇦", "+39"), "Venezuela": ("🇻🇪", "+58"),
    "Vietnam": ("🇻🇳", "+84"), "Yemen": ("🇾🇪", "+967"), "Zambia": ("🇿🇲", "+260"), "Zimbabwe": ("🇿🇼", "+263")
}

def get_country_info(file_name):
    clean = file_name.rsplit('.', 1)[0].replace('-', ' ').replace('_', ' ').strip().title()
    for country in COUNTRY_DB:
        if country.lower() in clean.lower():
            return country, COUNTRY_DB[country][0], COUNTRY_DB[country][1]
    
    # Common Shortcut Fixes
    if "Usa" in clean: return "USA", "🇺🇸", "+1"
    if "Uk" in clean: return "UK", "🇬🇧", "+44"
    if "Saudi" in clean: return "Saudi Arabia", "🇸🇦", "+966"
    
    return clean.split()[0], "🏳️", ""

def get_available_files():
    files_data = {}
    if os.path.exists(DOWNLOAD_PATH):
        all_files = sorted([f for f in os.listdir(DOWNLOAD_PATH) if f.endswith(".txt")])
        for file in all_files:
            name, flag, code = get_country_info(file)
            display = f"{flag} {name}"
            files_data[display] = {"file": file, "code": code}
    return files_data

def countries_menu():
    files = get_available_files()
    markup = InlineKeyboardMarkup(row_width=1)
    if not files: return None
    for display in files.keys():
        markup.add(InlineKeyboardButton(display, callback_data=f"sel_{display}"))
    markup.add(InlineKeyboardButton("🔄 Reset List", callback_data="reset_list"))
    return markup

def actions_menu(display, n1, n2):
    markup = InlineKeyboardMarkup()
    # ORIGINAL STYLE: Numbers on buttons
    markup.add(InlineKeyboardButton(f"❐ 📱 {n1}", callback_data="copy_hint"))
    markup.add(InlineKeyboardButton(f"❐ 📱 {n2}", callback_data="copy_hint"))
    markup.add(InlineKeyboardButton("🔄 Get New Numbers", callback_data=f"sel_{display}"))
    markup.add(InlineKeyboardButton("🌍 Back to Menu", callback_data="back"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "--- 🌍 Select Country ---", reply_markup=countries_menu())

@bot.callback_query_handler(func=lambda call: True)
def handle_clicks(call):
    chat_id, msg_id = call.message.chat.id, call.message.message_id
    files = get_available_files()

    if call.data == "copy_hint":
        bot.answer_callback_query(call.id, "Click numbers below to copy!", show_alert=False)

    elif call.data == "back" or call.data == "reset_list":
        bot.edit_message_text("--- 🌍 Select Country ---", chat_id, msg_id, reply_markup=countries_menu())

    elif call.data.startswith("sel_"):
        display = call.data.replace("sel_", "")
        info = files.get(display)
        if info:
            path = os.path.join(DOWNLOAD_PATH, info['file'])
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    nums = [l.strip() for l in f.readlines() if l.strip()]
                    if len(nums) >= 2:
                        s = random.sample(nums, 2)
                        def fmt(n, c):
                            clean = n.replace(c, "").replace("+", "").strip()
                            return f"{c} {clean}"
                        
                        n1, n2 = fmt(s[0], info['code']), fmt(s[1], info['code'])
                        
                        # Interface wahi purana, aur click-to-copy message ke andar
                        res = (f"📍 **Country:** {display}\n"
                               f"📞 **Code:** `{info['code']}`\n\n"
                               f"📋 **Click to Copy:**\n`{n1}`\n`{n2}`")
                        
                        bot.edit_message_text(res, chat_id, msg_id, reply_markup=actions_menu(display, n1, n2), parse_mode="Markdown")
            except: pass

bot.polling(none_stop=True)
