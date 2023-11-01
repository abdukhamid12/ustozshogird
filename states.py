from aiogram.dispatcher.filters.state import StatesGroup, State

class SherikKerakState(StatesGroup):
  fio = State()
  texnologiya = State()
  aloqa = State()
  hudud = State()
  narxi = State()
  kasbi = State()
  murojat_vaqti = State()
  maqsad = State()

class IshJoyiKerakState(StatesGroup):
  fio = State()
  age = State()
  texnologiya = State()
  aloqa = State()
  hudud = State()
  narxi = State()
  kasbi = State()
  murojat_vaqti = State()
  maqsad = State()

class HodimKerakState(StatesGroup):
  idora = State()
  texnologiya = State()
  aloqa = State()
  hudud = State()
  fio = State()
  murojat_vaqti = State()
  ish_vaqti = State()
  maosh = State()
  info = State()

class UstozKerakState(StatesGroup):
  fio = State()
  age = State()
  texnologiya = State()
  aloqa = State()
  hudud = State()
  narxi = State()
  kasbi = State()
  murojat_vaqti = State()
  maqsad = State()

class ShogirtKerakState(StatesGroup):
  fio = State()
  age = State()
  texnologiya = State()
  aloqa = State()
  hudud = State()
  narxi = State()
  kasbi = State()
  murojat_vaqti = State()
  maqsad = State()