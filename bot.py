import telebot
from telebot import types
# from config import TOKEN

bot = telebot.TeleBot('6257056357:AAFw-6Ye4ES85cnA4jXEijSFZ8rlVZ8kafM') 
@bot.message_handler (commands = ['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    numer1 = types.KeyboardButton('restourant')
    markup.add(numer1)
    bot.send_message(message.chat.id,'привет дорогой гость '.format (message.from_user),reply_markup = markup)
    bot.send_photo (message.chat.id,open ('./static/11.jpeg',mode = 'rb'))

@bot.message_handler(content_types=['text'])

def bot_message (message):
    if message.chat.type == 'private':
        if message.text == 'restourant':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton('picca')
            item2 = types.KeyboardButton('sushi')
            item3 = types.KeyboardButton('burgers')
            markup.add (item,item2,item3)
            bot.send_message(message.chat.id ,' Что будем заказывать?'.format (message.from_user),reply_markup = markup)




        elif message.text == 'picca':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item4 = types.KeyboardButton('peperoni')
            item5 = types.KeyboardButton('italiano')
            item6 = types.KeyboardButton('chilli')
            item7 = types.KeyboardButton('◀️назад')
            markup.add (item4,item5,item6,item7)
            bot.send_message(message.chat.id,'какую пиццу вы хотите'.format (message.from_user),reply_markup=markup )

        elif message.text == '◀️назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton('picca')
            item8 = types.KeyboardButton('sushi')
            item9 = types.KeyboardButton('burgers')
            markup.add (item,item8,item9)
            bot.send_message(message.chat.id ,' Что будем заказывать?'.format (message.from_user),reply_markup = markup)


        elif message.text == 'peperoni':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,'Данный вид салями появился в Италии. Свое название она получила благодаря одному из главных ингредиентов — острому, стручковому перцу. Именно слово Pepe, что означает стручковый перец, легло в его основу. Поэтому само название должно вам указывать на то, что блюдо, которое вы получите, будет очень острым.'.format (message.from_user),reply_markup = markup)
            bot.send_photo (message.chat.id,open ('./static/12.jpg',mode = 'rb'))


        elif message.text == 'italiano':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,'Для ценителей итальянской пиццы — лучшие ингредиенты на тонком тесте: томатный соус с чесночком, сыр Premium, маринованное мясо, курица копчёная, грибы шампиньоны, куриные грудки, оливки, копчёная колбаса, свежие помидорки, маслинки.'
.format (message.from_user),reply_markup =markup)
            bot.send_photo (message.chat.id,open ('./static/13.jpg',mode = 'rb'))



        elif message.text == 'chilli':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
            bot.send_message(message.chat.id,'Пицца Чили. Говяжий фарш, острые перчики, болгарский перец, томаты, специи, сыр моцарелла. Chili Pizza. Minced beef, chili pepper, bell pepper, tomatoes, spices, mozzarella cheese.'.format (message.from_user),reply_markup = markup)
            bot.send_photo (message.chat.id,open ('./static/14.jpg',mode = 'rb'))


        elif message.text == 'sushi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
            item10 = ("California rolls")
            item11 = ('Philadelphia rolls')
            item12 = ("Alaska rolls")
            item13 = ('◀️назад')
            markup.add(item10,item11,item12,item13)
            bot.send_message(message.chat.id,'какие суши вы будете?'.format (message.from_user),reply_markup = markup)



        elif message.text == "California rolls":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)      
            bot.send_message(message.chat.id,'Считается, что ролл «Калифорния» был создан в 1973 году Итиро Маситой, шеф-поваром ресторана Tokyo Kaikan в Лос-Анджелесе. В 80-х годах он распространился и по другим штатам, потом стал известен в Японии, а затем — во всём мире. '.format (message.from_user),reply_markup = markup)
            bot.send_photo (message.chat.id,open ('./static/15.jpg',mode = 'rb'))


        elif message.text == ('Philadelphia rolls'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)       
            bot.send_message(message.chat.id,'Впервые такие роллы были приготовлены в 80-х годах поваром в Америке. Он очень увлекся сочетанием сырой рыбы и сыра филадельфия, которые попробовал в бейглах, что решил создать свой кулинарный шедевр. Бейгл – это хлебобулочный продукт, напоминающий бублик, который имеет разные начинки.'.format (message.from_user),reply_markup = markup)
            bot.send_photo (message.chat.id,open ('./static/16.jpg',mode = 'rb'))




        elif message.text == ("Alaska rolls"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)      
            bot.send_message(message.chat.id,'На самом деле существует масса рецептов приготовления "Аляски", ведь готовя ее в домашних условиях, вы сами решаете, какой ингредиент положить, а какой заменить или не использовать вовсе. Но всё же существует определённый состав, который сформирован уже много лет назад. Для того чтобы приготовить этот ролл у себя дома или ускорить процесс выбора порции в ресторане, достаточно запомнить совершенно несложный список ингредиентов:'.format (message.from_user),reply_markup = markup)
            bot.send_photo (message.chat.id,open ('./static/17.jpeg',mode = 'rb'))


        elif message.text == ('◀️назад'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
            item = types.KeyboardButton('picca')
            item8 = types.KeyboardButton('sushi')
            item9 = types.KeyboardButton('burgers')
            markup.add (item,item8,item9)
            bot.send_message(message.chat.id ,' Что будем заказывать?'.format (message.from_user),reply_markup = markup)


        elif message.text == ('burgers'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
            item14 = ("Umami Burger, Лос-Анджелес")
            item15 = ('Bleecker Street Burger')
            item16 = ("Gordon Ramsay Burger at Planet Hollywood Resort & Casino, Ласс")
            item17 = ('◀️назад')   
            markup.add (item14,item15,item16,item17)
            bot.send_message(message.chat.id ,' какие бургеры вы будете ?'.format (message.from_user),reply_markup=markup)

        elif message.text == ("Umami Burger, Лос-Анджелес"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
            bot.send_message(message.chat.id,'На Ла-Бреа-авеню в Лос-Анджелесе в 2009 году открылся ресторанчик Umami Burger, что позднее перерос в сеть из более чем 20 заведений. Их владелец шеф-повар и винодел Адам Флейшман был самоучкой, а стал успешным ресторатором благодаря умами – необычному вкусу высокобелковых веществ. В Азии умами является отдельным вкусом, в дополнение к привычным острому, сладкому, соленому и кислому. Он присутствует в продуктах, насыщенных белками, например, в сыре или говядине. Флейшман был настолько впечатлен, что решил воплотить умами в бургере. Он хотел отойти от традиционного способа приготовления этого блюда и изобрести нечто новое. Повар взял за основу соус хойсин, дополнил его японскими грибами шиитаке, жареным помидором, обжаренным с анисом луком и выдержанным пармезаном. Все это Адам поместил в португальскую булочку с молоком. Необычный рецепт пришелся клиентам по душе, и сеть Umami Burger только растет.')
            bot.send_photo(message.chat.id,open('./static/f12.jpg',mode = 'rb'))

      

        elif message.text == ('Bleecker Street Burger'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,'Сочный Bleecker burger дважды был признан Time Out London лучшим бургером в Лондоне. Отведать его можно в одноименном фудтраке, колесящем по улицам города, и в  небольшой закусочной на Victoria Street, где несмотря на скромный ассортимент, всегда очередь. Посетители признаются, что вкус бургера буквально кружит голову и вызывает зависимость. Сочетание высококачественной говядины с английских фермерских пастбищ, свежей булочки с кунжутом и самодельного соуса для бургеров - вот секрет успеха Bleecker burger. Главное правило его создателей   - не экономить на ингредиентах.  Именно поэтому клиенты не скупятся и платят за знаменитые бургеры в среднем по 8 фунтов. Секрет приготовления Bleecker street burger - в составе фарша, куда входит 3 типа мяса: говядина, ребрышки и немного костного мозга.  Поджаренные на гриле котлеты полейте соусом для барбекю Hellmann')
            bot.send_photo(message.chat.id,open('./static/f13.jpg',mode = 'rb'))


        elif message.text == ("Gordon Ramsay Burger at Planet Hollywood Resort & Casino, Ласс"):
             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)   
             bot.send_message(message.chat.id ,'Гордон Рамзи – прославленный шеф-повар и буквально все, что он готовит, сразу приобретает огромную популярность. Так случилось и с тремя бургерами от Рамзи. The Hog Burger, American Burger и Truffle Burger, которые можно попробовать исключительно в Вегасе, просто шикарны. Их секрет в том, что говяжьи ребрышки и грудинка обжариваются на открытом огне с отборным маслом из графства Дэвон. А особый рецепт с уткой, чеддером и обжаренным яйцом не имеет аналогов. Ресторан на 200 мест всегда забит под завязку. По словам исполнительного шеф-повара Кристины Уилсон, в день посетители заказывают более 1400 бургеров. И заведение остается одним из самых посещаемых при высокой конкуренции именно благодаря им.'.format (message.from_user),reply_markup = markup)
             bot.send_photo(message.chat.id,open('./static/f14.jpg',mode = 'rb'))

bot.polling(non_stop=True)

        




        









    