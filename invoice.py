from dataclasses import dataclass
from aiogram import types

from config import PROVIDER_TOKEN


@dataclass
class Item:
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: list[types.labeled_price.LabeledPrice]
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False
    provider_token: str = PROVIDER_TOKEN

    def generate_invoices(self):
        return self.__dict__

# товары

action_games = [Item(
   title='Warframe',
   description='Пробудитесь в роли неудержимого воина и сражайтесь вместе с друзьями в этой сюжетной бесплатной онлайн-игре. '
               'Столкнитесь с враждующими фракциями в обширной межпланетной системе, следуя указаниям загадочной Лотос, повышайте уровень своего Варфрейма, создайте арсенал разрушительной огневой мощи,'
               ' и откройте свой истинный потенциал в огромных открытых мирах этого захватывающего сражения от третьего лица.',
   currency='RUB',
   prices=[
       types.labeled_price.LabeledPrice(
           label='Warframe',
           amount=1_500_00
       )

   ],
   start_parameter='create_invoice_warframe',
   photo_url="https://cdn.akamai.steamstatic.com/steam/apps/230410/header.jpg?t=1684438098",
   photo_size=600,
   need_shipping_address=True,
   is_flexible=True
),
    Item(
        title='DayZ',
        description='В этой игре не будет маркеров на карте, ежедневных заданий или списков лидеров, что поможет вам создать свою историю.'
                    ' В ней есть лишь Чернарусь — постсоветское государство площадью 230 квадратных километров, которое поразил неизвестный вирус,'
                    ' превративший большую часть ее населения в свирепствующих зараженных.',
        currency='RUB',
        prices=[
            types.labeled_price.LabeledPrice(
                label='DayZ',
                amount=1_000_00
            )

        ],
        start_parameter='create_invoice_DayZ',
        photo_url="https://cdn.akamai.steamstatic.com/steam/apps/221100/header.jpg?t=1674143992",
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    ),

    Item(
        title='NARAKA: BLADEPOINT',
        description='NARAKA: BLADEPOINT — это «королевская битва» для 60 человек, вдохновленная мифами и легендами Дальнего Востока',
        currency='RUB',
        prices=[
            types.labeled_price.LabeledPrice(
                label='NARAKA: BLADEPOINT',
                amount=1_000_00
            )

        ],
        start_parameter='create_invoice_NARAKA',
        photo_url="https://cdn.akamai.steamstatic.com/steam/apps/1203220/header.jpg?t=1683170532",
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    )
]


MMO_games = [Item(
   title='Summoners War: Chronicles',
   description='Королевство Рахиль ищет призывателей, способных противостоять Тефо.'
               ' Начинается ваша история в Рахильской страже! Изучайте огромный мир вокруг, призывайте монстров и наслаждайтесь новой RPG в мире Summoners War.',
   currency='RUB',
   prices=[
       types.labeled_price.LabeledPrice(
           label='Summoners War: Chronicles',
           amount=500_00
       )

   ],
   start_parameter='create_invoice_Summoners',
   photo_url="https://cdn.akamai.steamstatic.com/steam/apps/2167580/header.jpg?t=1684992880",
   photo_size=600,
   need_shipping_address=True,
   is_flexible=True
),
    Item(
        title='Destiny 2',
        description='Destiny 2 – это экшен-MMO в едином развивающемся мире, к которому вы с друзьями можете присоединиться где и когда угодно, абсолютно бесплатно.',
        currency='RUB',
        prices=[
            types.labeled_price.LabeledPrice(
                label='Destiny 2',
                amount=100_00
            )

        ],
        start_parameter='create_invoice_Destiny',
        photo_url="https://cdn.akamai.steamstatic.com/steam/apps/1085660/header_russian.jpg?t=1684966156",
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    ),

    Item(
        title='Will To Live Online',
        description='Will To Live - MMORPG-шутер, действие которого разворачивается в суровом постапокалиптическом мире.'
                    ' Исследуй мир, вступай в схватки с мутантами и с другими выжившими, вступай в кланы в борьбе за существование и докажи свое право на Жизнь.',
        currency='RUB',
        prices=[
            types.labeled_price.LabeledPrice(
                label='Will To Live Online',
                amount=100_00
            )

        ],
        start_parameter='create_invoice_Will',
        photo_url="https://cdn.akamai.steamstatic.com/steam/apps/707010/header_russian.jpg?t=1667809610",
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    )
]

RPG_games = [Item(
   title='Stardew Valley',
   description='Вам досталась старая дедушкина ферма в долине Стардью.'
               ' С горстью монет в кармане и старыми инструментами в руках вы начинаете новую жизнь. Сможете ли вы превратить пустырь в цветущий сад?',
   currency='RUB',
   prices=[
       types.labeled_price.LabeledPrice(
           label='Stardew Valley',
           amount=300_00
       )

   ],
   start_parameter='create_invoice_Stardew',
   photo_url="https://cdn.akamai.steamstatic.com/steam/apps/413150/header.jpg?t=1666917466",
   photo_size=600,
   need_shipping_address=True,
   is_flexible=True
),
    Item(
        title='Brotato',
        description='Brotato — аренный шутер с элементами «рогалика», в котором вы играете за вооруженную картофелину,'
                    ' дающую отпор ордам пришельцев. Берите до 6 видов оружия, выбирайте черты и предметы, придумывайте тактику и выживайте до прибытия подмоги.',
        currency='RUB',
        prices=[
            types.labeled_price.LabeledPrice(
                label='Brotato',
                amount=100_00
            )

        ],
        start_parameter='create_invoice_Brotato',
        photo_url="https://cdn.akamai.steamstatic.com/steam/apps/1942280/header.jpg?t=1677509097",
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    ),

    Item(
        title='ELDEN RING',
        description='НОВЫЙ ФЭНТЕЗИЙНЫЙ РОЛЕВОЙ БОЕВИК. Восстань, погасшая душа! Междуземье ждёт своего повелителя.'
                    ' Пусть благодать приведёт тебя к Кольцу Элден.',
        currency='RUB',
        prices=[
            types.labeled_price.LabeledPrice(
                label='ELDEN RING',
                amount=100_00
            )

        ],
        start_parameter='create_invoice_ELDEN',
        photo_url="https://cdn.akamai.steamstatic.com/steam/apps/1245620/header.jpg?t=1683618443",
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    )
]

# доставка
POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[types.LabeledPrice('Почтой', 200_00)]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Почтой ускоренная',
    prices=[types.LabeledPrice('Почтой ускоренная', 1000_00)]
)