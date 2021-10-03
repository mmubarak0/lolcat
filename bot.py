#!/usr/bin/env python
# pylint: disable=C0116,W0613


import logging
import random
import os
import Messages


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

intro = Messages.intro

fortunes = Messages.fortunes
content_types = ["text", "sticker", "pinned_message",
                 "photo", "audio", "document", "sticker",
                 "video", "video_note", "migrate_to_chat_id", "migrate_from_chat_id"]


lisa = []
lisaid = []
stuff = {}

def echo(update: Update, context: CallbackContext):
    """ text handler
        it also return the message id for me
        if i need it
        & it handles query send too
    """

    # send a fortune message when this function is called
    # here i used BSD fortune
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=os.popen('fortune fortune').read())

    # At first it checks for the text type
    # if it's coming from query it or not
    # and handle the error if it was not
    try:
        # Well here I used my username to show command as an admin
        # or somthing like nobody else than me can see it
        if update.callback_query.message.chat.username == 'coruten':
            print("file_id: " + str(update.callback_query.message.message_id))
            lisaid.append(update.callback_query.message.message_id)
    except Exception:
        if update.message.chat.username == 'coruten':
            print("file_id: " + str(update.message.message_id))
            lisaid.append(update.message.message_id)



def voice_handler(update: Update, context: CallbackContext):
    """ voice handler it also return the voice message id for me if i need it """
    # file = context.bot.getFile(update.message.voice.file_id)
    if update.message.chat.username == 'coruten':
        print("file_id: " + str(update.message.voice.file_id))
        # file.download('voice.ogg')


def document_handler(update: Update, context: CallbackContext):
    """ Documents handler it also return the document message id for me if i need it """
    if update.message.chat.username == 'coruten':
        print("file_id: " + str(update.message.document.file_id))


def video_handler(update: Update, context: CallbackContext):
    """ Video handler it also return the video id for me if i need it """
    if update.message.chat.username == 'coruten':
        print("file_id: " + str(update.message.video.file_id))


def photo_handler(update: Update, context: CallbackContext):
    """ Photo handler it also return the photo id for me if i need it """
    if update.message.chat.username == 'coruten':
        print("file_id: " + str(update.message.photo[0]['file_id']))
        context.bot.send_photo(update.message.chat.id,
                               update.message.photo[0]['file_id'])


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("♦️ ميكانيكا المواد", callback_data='1'),
            InlineKeyboardButton(
                "♦️ التشريح و وظائف الأعضاء", callback_data='2'),
            InlineKeyboardButton(
                "♦️ نظرية الدوائر الكهربية", callback_data='3'),
        ],
        [InlineKeyboardButton("♥️ أساسيات الهندسة الطبية", callback_data='4')],
        [InlineKeyboardButton("🔸 الكيمياء العضوية", callback_data='5')],
        [InlineKeyboardButton("💻 لغات البرمجة", callback_data='6')],
        [
            InlineKeyboardButton(
                "🔹 الدوال التكاملية الخاصة", callback_data='7'),
            InlineKeyboardButton("🔹 الدوال المركبة", callback_data='8'),
        ],
        [InlineKeyboardButton("💡مراجع", callback_data='9')],
        [InlineKeyboardButton("🎲 Apps", callback_data='10')],
    ]

    # I didn't completed the adding stuff from the bot
    # mechanism but at least I will try to complete this
    # later so now I will Just Hard coded stuff .

    # adding button for the admin to add stuff
    if update.message.chat.username == "coruten":
        keyboard.append([InlineKeyboardButton(
            "add stuff", callback_data="add")])

    # define the keyboards button handler
    reply_markup = InlineKeyboardMarkup(keyboard)

    # reply to user with the button under the message after sending /start
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    # query.edit_message_text(text=f"{query.data}")
    # `query.data` just return the key given from the query answer
    # and it's equall to `callback_data` parameter in keyboard buttons
    """ Mechanics of materials stuff """
    if query.data == '1':
        keyboard = [
            [
                InlineKeyboardButton("Main sheet", callback_data='mecha1'),
                InlineKeyboardButton("Exams", callback_data='mecha2'),
                InlineKeyboardButton("Youtube tutor", callback_data='mecha3'),
            ],
            [
                InlineKeyboardButton("hand summaries", callback_data='mecha4'),
                InlineKeyboardButton("Lectures old", callback_data='mecha5'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query

        # here we used the `edit_message_test` to overwrite the previous
        # message and replace it with the new one instead
        # having multiple replys
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ Anatomy stuff """
    if query.data == '2':
        keyboard = [
            [
                InlineKeyboardButton("Lectures", callback_data='anatomy1'),
                InlineKeyboardButton("pdf", callback_data='anatomy2'),
            ],
            [
                InlineKeyboardButton(
                    "YouTube tutor", callback_data='anatomy3'),
                InlineKeyboardButton("Lab", callback_data='anatomy4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ Circuit theory stuff """
    if query.data == '3':
        keyboard = [
            [
                InlineKeyboardButton("Introduction", callback_data='elec1'),
                InlineKeyboardButton("Lab", callback_data='elec2'),
            ],
            [
                InlineKeyboardButton("Lectures", callback_data='elec3'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ BME principles stuff """
    if query.data == '4':
        keyboard = [
            [
                InlineKeyboardButton("Videos", callback_data='bme1'),
                InlineKeyboardButton("PDF", callback_data='bme2'),
                InlineKeyboardButton("PPT", callback_data='bme3'),
            ],
            [
                InlineKeyboardButton("Youtube tutor", callback_data='bme4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ Organic chemistry stuff """
    if query.data == '5':
        keyboard = [
            [
                InlineKeyboardButton("PPT", callback_data='chem1'),
                InlineKeyboardButton("PDF", callback_data='chem2'),
            ],
            [
                InlineKeyboardButton("Old lectures", callback_data='chem3'),
                InlineKeyboardButton("Exams", callback_data='chem4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ Programming language stuff """
    if query.data == '6':
        keyboard = [
            [
                InlineKeyboardButton("Lectures", callback_data='code1'),
            ],
            [
                InlineKeyboardButton("Lab", callback_data='code2'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ Special integral stuff """
    if query.data == '7':
        keyboard = [
            [
                InlineKeyboardButton("Lectures", callback_data='integral1'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ Complex number stuff """
    if query.data == '8':
        keyboard = [
            [
                InlineKeyboardButton("Master sheet", callback_data='comp1'),
                InlineKeyboardButton("Exams", callback_data='comp2'),
            ],
            [
                InlineKeyboardButton("hand summaries", callback_data='comp3'),
                InlineKeyboardButton("YouTube tutor", callback_data='comp4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ references stuff """
    if query.data == '9':
        keyboard = [
            [
                InlineKeyboardButton(
                    "Complex Numbers", callback_data='compref'),
            ],
            [
                InlineKeyboardButton(
                    "Mechanics of materials", callback_data='mecharef'),
            ],
            [
                InlineKeyboardButton("Anatomy & physiology",
                                     callback_data='anatomyref'),
            ],
            [
                InlineKeyboardButton(
                    "Biomedical Engineering principles", callback_data='bmeref'),
            ],
            [
                InlineKeyboardButton("Organic chemistry",
                                     callback_data='chemref'),
            ],
            [
                InlineKeyboardButton("Programming language",
                                     callback_data='coderef'),
            ],
            [
                InlineKeyboardButton("Special integral",
                                     callback_data='integralref'),
            ],
            [
                InlineKeyboardButton(
                    "Complex number", callback_data='compref'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)
    """ Apps stuff """
    if query.data == '10':
        keyboard = [
            [
                InlineKeyboardButton("Anatomy ", callback_data='app1'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)

    if query.data == 'back':
        keyboard = [
            [
                InlineKeyboardButton("♦️ ميكانيكا المواد", callback_data='1'),
                InlineKeyboardButton(
                    "♦️ التشريح و وظائف الأعضاء", callback_data='2'),
                InlineKeyboardButton(
                    "♦️ نظرية الدوائر الكهربية", callback_data='3'),
            ],
            [InlineKeyboardButton(
                "♥️ أساسيات الهندسة الطبية", callback_data='4')],
            [InlineKeyboardButton("🔸 الكيمياء العضوية", callback_data='5')],
            [InlineKeyboardButton("💻 لغات البرمجة", callback_data='6')],
            [
                InlineKeyboardButton(
                    "🔹 الدوال التكاملية الخاصة", callback_data='7'),
                InlineKeyboardButton("🔹 الدوال المركبة", callback_data='8'),
            ],
            [InlineKeyboardButton("💡مراجع", callback_data='9')],
            [InlineKeyboardButton("🎲 Apps", callback_data='10')],
        ]

        if update.effective_chat.username == "coruten":
            keyboard.append([InlineKeyboardButton(
                "add stuff", callback_data="add")])

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)

# -----------------------------------------------------------------------------------------------
    """ answering & sending files """

    """ Mechanic Answers """
    if query.data == 'mecha1':
        # echo is just a place holder for now
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIBoGFY2F96ou-eBL2v22RExkn0VTlTAAK_CgACnIPQUSVMXXAZfbQOIQQ')
    elif query.data == 'mecha2':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICo2FZ65KP0RzXR7kCVMBZj7ka6RQAA78KAAIxIVFSkCOtx4T_GdwhBA')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICpGFZ65LAy_V4mHt4DQx529oOcLWIAALACgACMSFRUlpfpbzcC4_yIQQ')
    elif query.data == 'mecha3':
        # echo(update, context)
        context.bot.send_message(
            query.message.chat.id, 'https://youtube.com/playlist?list=PLEYqyyrm-hQ3wtF34smyJSAOqUJqnf1ch')
    elif query.data == 'mecha4':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICp2FZ7N-K5Wzy__OBFugcYnqf4KpiAAKzCgACMSFRUnxsdBjOBfftIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICqGFZ7N_WFhUM8IeQ7DpvQ3d6RJxAAAK1CgACMSFRUvWekLBLUxNzIQQ')
    elif query.data == 'mecha5':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICqWFZ7VZ1HF_xTDqZatKfdhcDrIHpAAK2CgACMSFRUjpRBLKYrRViIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICqmFZ7VbRov_5b9Oa6dy3C0V8rbBYAAK3CgACMSFRUlZS0qzdQUPMIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICq2FZ7Vby5skOYRik7yPti6DFLku1AAK4CgACMSFRUnxwA5smHcYdIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICrGFZ7VaXb56RaKgeZX9KWlr4M01TAAK5CgACMSFRUj1ptuBdsQ2YIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICrWFZ7VZbGKj0Ozyi1tNwzU0FH1irAAK6CgACMSFRUoMrhfDQCi7FIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICrmFZ7VZ8FI6AOZhcREyxhbJTCVejAAK7CgACMSFRUj-ovvLlViX4IQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICr2FZ7VZdFq_uPkGXdSZ5ApNjyXpcAAK8CgACMSFRUnSiC7uCRsXHIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICsGFZ7VaeRTpxgBIOvKyzM0MSsK4CAAK9CgACMSFRUqtTFKgxycPaIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAICsWFZ7VYvz4HQ-ygtJWKCl3S0eTUTAAK-CgACMSFRUhDcdxorKpjGIQQ')

    """ Anatomy Answers """
    if query.data == 'anatomy1':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC4WFZ_ZWw5b7qldztRGBPkIRgLWorAAI9CwACTik4Uj8O39CLrs3kIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC4mFZ_ZWnf8Xq-KgpXODUmBjXq0haAAI-CwACTik4UtMXJk94hcVUIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC42FZ_ZXPc92RF2uQh5SNtBBvQb_wAAI_CwACTik4Ujomq8u_GMuRIQQ')
    elif query.data == 'anatomy2':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC5GFZ_iiI16Q6K9WQknMNdC2zgxLoAAKuCgAD1mlSXxK4ilAyZ80hBA')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC5WFZ_ii3k8_lI1Yzq3r1Cfn2ipT0AAKvCgAD1mlSZB8IWWwxoj8hBA')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC5mFZ_igpsSComsYMDz9WNzMW8OiaAAKwCgAD1mlSMD4YzcI8w-chBA')
    elif query.data == 'anatomy3':
        # echo(update, context)
        context.bot.send_message(
            query.message.chat.id, 'https://www.youtube.com/playlist?list=PL2vrmieg9tO1TE2BEft0UWG6lkMYCWXGY')
    elif query.data == 'anatomy4':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC52FZ_r3H3pX-YrtFeSSpDYmND7AwAAKQCwACg9OgUqt3NJve234FIQQ')
        context.bot.send_video(
            query.message.chat.id, 'BAACAgQAAxkBAAIC6GFZ_r2C9KT0wEiWvumzX7IEJSgqAAKSCwACg9OgUklMD77kYFXyIQQ')

    """ Circuit theory stuff """
    if query.data == 'elec1':
        # echo(update, context)
        context.bot.send_message(
            query.message.chat.id, intro)
    elif query.data == 'elec2':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIC7WFaAAGEg1iZ0FHjcmshwTUY7G2JHgACswwAAk4pQFJb9ihZ5IEpsiEE')
    elif query.data == 'elec3':
        echo(update, context)


    """ BME principles stuff """
    if query.data == 'bme1':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDA2FaA8DZP4scok3ZKHS7JMG2m_vrAAL6CwACGHc4UnrCTf6U1VdAIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDBGFaA8CWwttT80B087W5LdfQwyNtAAJ2CAACishwUtLYb_PTz7NvIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDBWFaA8ClkGouWFsJ1g-qf1wYqY_yAAJ1CAACishwUvpX907bZu5yIQQ')
    elif query.data == 'bme2':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDBmFaBG68nALrbPqF7pvsxOWT_J5SAAIdCQAD1mFSuJ72mufB3qwhBA')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDB2FaBG5G6QrRjSqrdL8PyigG014NAAIeCQAD1mFSdmfa_A06lg8hBA')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDCGFaBHi1NCjSsfJQHb22N9-liVhzAAKXCgACd55IUqr6XnQy5QkFIQQ')
    elif query.data == 'bme3':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDCWFaBNE331j_1NtF01XdpNqn9qbHAALqCwACMO9ZUmA1eG8KVsn9IQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDCmFaBNGBZx1kjW-5C-EtfOS7iacTAAL-CwACMO9ZUsArkOfyYXnRIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDC2FaBNEPnuzV0T5KEHR05UZca6VvAAKNCAACMO9hUhMAAUWwuYq0zCEE')
    elif query.data == 'bme4':
        # echo(update, context)
        context.bot.send_message(
            query.message.chat.id, 'https://youtu.be/qEfQSL7yVo0')
        context.bot.send_message(
            query.message.chat.id, 'https://youtu.be/FD9G_foVk30')

    """ Organic chemistry stuff """
    if query.data == 'chem1':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDDGFaBX1lhzF6KQVE3hQpUotRuyRfAALkCQAC70dhUpCGR4U7mzfmIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDDWFaBX0wDLFyW1efqJSjjGyjlNJEAALlCQAC70dhUmCyFK_LuSp_IQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDDmFaBX0tHXEw1AABfXs30TDBosJWoQACXAsAAoPTqFJAS-CT6v3YAiEE')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDD2FaBX2zHlT46wwGYSA3hzEEKioHAAJdCwACg9OoUq_KX2YguqeEIQQ')
    elif query.data == 'chem2':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDEGFaBdSjI7ALnRn_k0uD0YfSDv5HAAIQCQAD1mFSH6rbxpG-i2chBA')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDEWFaBdSGUKBkk-_tHMbr0xaTZI9jAAIRCQAD1mFSNvbufZTfAAGFIQQ')
    elif query.data == 'chem3':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDEmFaBmTGeoJmX4t5qbQXaCpV8h85AAKqCgACMSFRUjbt2tVBBGpxIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDE2FaBmTY8X7qHDyT5F37w9SlUxSCAAKrCgACMSFRUu4UINkwp-AFIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDFGFaBmSYAqNZlkO_iB2hhMGFHo9cAAKsCgACMSFRUkGLThQyKZIyIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDFWFaBmTfOFA9ZkOlMHC5-YO3AAEI1AACrQoAAjEhUVJ__ae-JPkgfCEE')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDFmFaBmR7HNhZMuQlf4nLwguOKGOCAAKuCgACMSFRUqT64zIIEEybIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDF2FaBmQE9DAE5OcQ42lk9GtlAY6oAAKvCgACMSFRUnmo3TnoU6hJIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDGGFaBmShYDzyKh4BOGf9_0wy9GsLAAKwCgACMSFRUr0Doih7CX8rIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDGWFaBmS0I1O6s7zKg85xX7gTMs1uAAKxCgACMSFRUhu1hBpOrEjZIQQ')
    elif query.data == 'chem4':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgUAAxkBAAIDGmFaBtJtoXan4yRK_3z2EdtP-i0hAALhAgAC9-ZRVvEjZRYt5GVEIQQ')

    """ Programming language stuff """
    if query.data == 'code1':
        echo(update, context)
    elif query.data == 'code2':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgUAAxkBAAIDG2FaBy6ldpbgMZHhztTRJRcZLx2dAAImBQACyA5hVpGKvfBzE5N3IQQ')

    """ Special integral stuff """
    if query.data == 'integral1':
        # echo(update, context)
        context.bot.send_video(
            query.message.chat.id, 'BAACAgQAAxkBAAIDHGFaB5cCMa8WAAELKbjpw-hx91nbvAACxAgAAi4CaVJM6T8GymwDSSEE')
        context.bot.send_video(
            query.message.chat.id, 'BAACAgQAAxkBAAIDHWFaB5eAUY68UKFPSC7bwUcUknbvAALGCAACLgJpUiQu3vyuo_y6IQQ')
        context.bot.send_video(
            query.message.chat.id, 'BAACAgQAAxkBAAIDHmFaB5c6o-qZPFyfgQqDaZMLYhOXAALeCQAC_EOoUkP5cXapZnSiIQQ')

    """ Complex number stuff """
    if query.data == 'comp1':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDH2FaCBIb-pwBqAjXCIxHwT1CezuHAALaDwACe9vxUeNXpdUUkIS1IQQ')
    elif query.data == 'comp2':
        # echo(update, context)
        context.bot.send_photo(
            query.message.chat.id, 'AgACAgQAAxkBAAIDIGFaCMIloFFoiU86TKXiBMgl-WRQAALTtjEbMSFJUtr-ylkgzWfMAQADAgADcwADIQQ')
        context.bot.send_photo(
            query.message.chat.id, 'AgACAgQAAxkBAAIDIWFaCMKz05vK_2dHSBaaTfMawQIlAALUtjEbMSFJUnbvYipGZboXAQADAgADcwADIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDJGFaCO47W25cTEPuN_uhUUuG6qvEAALiCgACMSFJUg7d-jciJAn8IQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDJWFaCO6cIZ9wmIUEivh-rHOo1eLrAAKpCQAC5dhIUhvwrkwg7IsIIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDJmFaCO5vxb2TRiN8l8YAAYKGEa-v1QACpgkAAuXYSFK6-YOOG2nxsiEE')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDJ2FaCO4BIroBRMjsDuVZDBlPmPjKAAKnCQAC5dhIUvMGB53EFozZIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDKGFaCO48dS9jMHPfmwTklMQ_j2MlAAKoCQAC5dhIUjKx_KrjiDNhIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDKWFaCO5Y_fB0O98UIU1lP91iGeO9AAKqCQAC5dhIUvVHZnTHW5oaIQQ')
    elif query.data == 'comp3':
        # echo(update, context)
        context.bot.send_message(
            query.message.chat.id, 'https://www.youtube.com/watch?v=BzzkGZlfVmg&index=1&list=PLBY4G2o7DhF0TSossUvJ-CTKSLfOhQgb6')
    elif query.data == 'comp4':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDLGFaCYcoiPmjX6068szMB68wWOudAAKnCgACMSFRUsVoY-uu1GYyIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDLWFaCYee5MLayNK2dc1qp56zZ6ceAAKoCgACMSFRUqx6IIPwa70HIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDLmFaCYcX4GdVyvXh-7L7VPPMJyJhAAKlCQAC5dhIUpqTsa2MAcS6IQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDL2FaCYfoupJpouYrg66lq9qx9YUAA6cJAALl2EhS8wYHncQWjNkhBA')

    """ references stuff """
    if query.data == 'mecharef':
        echo(update, context)
    elif query.data == 'anatomyref':
        echo(update, context)
    elif query.data == 'elecref':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDM2FaCnoMqoiGZcWyT2xsoYT_cZ5yAALSDAACTilAUtolkj0MscPFIQQ')
    elif query.data == 'bmeref':
        echo(update, context)
    elif query.data == 'chemref':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDNGFaCqUWeogfU09WD9AhxVtHHt6VAAKpDwAC9LlJUma-E1qIvfg9IQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDNWFaCqVfJvte2bwzSKjPEuYewfdbAALFDwAC9LlJUiJ_Z4qQiRIhIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDNmFaCqVZba0nFx6RNcqOx0WP8eruAALyDwAC9LlJUlV6ZAh24sI8IQQ')
    elif query.data == 'coderef':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDO2FaC9v6SWZSJQc9b2Nldmc1shEeAAIpEQAC6tZZUhuFrXySSRl7IQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDPGFaC9uaTUhDRLXmPz9Zte-6q1INAAItEQAC6tZZUpcerirqGPiDIQQ')
    elif query.data == 'integralref':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgUAAxkBAAIDN2FaCv70CEE6NCvOhwEAAWTv8m0dIAAC4gIAAvfmUVb08yfxEUrTrSEE')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDOGFaCv5lTbb4hDMaJfpbh8ps7hXSAAKDDwAC6tZpUkK58BAjPm0GIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDOWFaCv6jzIkO5FYJv10_beKCZYy5AAIMCwAD1mlSumhZ4ECECZ4hBA')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDOmFaCv5toEms7BMHQZUueLHAOj-_AAINCwAD1mlSa5811TcTsXkhBA')
        context.bot.send_message(
            query.message.chat.id, 'solution vol(1, 2) for `Advanced Engineering Mathematics`')
    elif query.data == 'compref':
        # echo(update, context)
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDMGFaCiKb78YQYvM-Cv4Q2aapWpBAAAKvCQAC5dhIUkTzlwNZtfKsIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDMWFaCiLQK1sB8Qt3qssJPSh0cuF_AAKxCQAC5dhIUpOPpJ2_xEYfIQQ')
        context.bot.send_document(
            query.message.chat.id, 'BQACAgQAAxkBAAIDMmFaCiLc7PrA2HQKJsWcenNENNWCAAK0EAAC9LlJUo7XPMgIrGxuIQQ')

    """ Apps stuff """
    if query.data == 'app1':
        echo(update, context)
# --------------------------------------------------------------------------------------------END of Answer section
    answers = ["amecha1", "amecha2", "amecha3", "amecha4", "amecha5",
               "aanatomy1", "aanatomy2", "aanatomy3", "aanatomy4",
               "aelec1", "aelec2", "aelec3",
               "abme1", "abme2", "abme3", "abme4",
               "achem1", "achem2", "achem3", "achem4",
               "acode1", "acode2",
               "aintegral1",
               "acomp1", "acomp2", "acomp3", "acomp4",
               ]
    if query.data == 'add':
        keyboard = [[InlineKeyboardButton("m1(Main sheet)", callback_data=answers[0]),
                     InlineKeyboardButton(
                         "m2(exam)", callback_data=answers[1]),
                     InlineKeyboardButton(
                         "m3(yt tutor)", callback_data=answers[2]),
                     InlineKeyboardButton(
                         "m4(hand summary)", callback_data=answers[3]),
                     InlineKeyboardButton(
                         "m5(lectures old)", callback_data=answers[4])
                     ],
                    [InlineKeyboardButton("a6(lecture)", callback_data=answers[5]),
                    InlineKeyboardButton(
                        "a2(pdf)", callback_data=answers[6]),
                    InlineKeyboardButton(
                        "a3(yt tutor)", callback_data=answers[7]),
                    InlineKeyboardButton(
                        "a4(lab)", callback_data=answers[8])
                     ],
                    [InlineKeyboardButton("e1(intro)", callback_data=answers[9]),
                    InlineKeyboardButton(
                        "e2(lab)", callback_data=answers[10]),
                    InlineKeyboardButton(
                        "e3(lectures)", callback_data=answers[11])
                     ],
                    [InlineKeyboardButton("b1(video)", callback_data=answers[12]),
                    InlineKeyboardButton(
                        "b2(pdf)", callback_data=answers[13]),
                    InlineKeyboardButton(
                        "b3(ppt)", callback_data=answers[14]),
                    InlineKeyboardButton(
                        "b4(yt tutor)", callback_data=answers[15])
                     ],
                    [InlineKeyboardButton("ch1(ppt)", callback_data=answers[16]),
                    InlineKeyboardButton(
                        "ch2(pdf)", callback_data=answers[17]),
                    InlineKeyboardButton(
                        "ch3(old lec)", callback_data=answers[18]),
                    InlineKeyboardButton(
                        "ch4(exam)", callback_data=answers[19])
                     ],
                    [InlineKeyboardButton("co1(lectuer)", callback_data=answers[20]),
                    InlineKeyboardButton(
                        "co2(lab)", callback_data=answers[21])
                     ],
                    [InlineKeyboardButton("i1(lectures)", callback_data=answers[22])
                     ],
                    [InlineKeyboardButton("c1(master sheet)", callback_data=answers[23]),
                    InlineKeyboardButton(
                        "c2(exams)", callback_data=answers[24]),
                    InlineKeyboardButton(
                        "c3(hand summ)", callback_data=answers[25]),
                    InlineKeyboardButton(
                        "c4(yt tutor)", callback_data=answers[26])
                     ],
                    ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)

    if query.data in answers:
        msg = ("do you want to add stuff to : " + str(query.data))
        lisa.append(query.data)
    # print(lisa)
    # print(lisaid)
    # stuff[lisa[-1]] = lisaid[-1]
    # if not stuff["amecha1"] in amecha1:
    #     amecha1.append(stuff["amecha1"])
    # if not stuff["amecha2"] in amecha2:
    #     amecha1.append(stuff["amecha2"])
    # if not stuff["amecha3"] in amecha3:
    #     amecha1.append(stuff["amecha3"])
    # print(amecha1)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("<YOUR-TOKEN>")
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(echo_handler)
    updater.dispatcher.add_handler(
        MessageHandler(Filters.voice, voice_handler))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.document, document_handler))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.video, video_handler))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.photo, photo_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
