import flet as ft

from datetime import datetime 

def main(page: ft.Page):
   
   page.title = 'мое первое приложение'
   page.theme_mode = ft.ThemeMode.LIGHT

   greeting_text = ft.Text("Hello World")
   greeting_history  = []
   history_text = ft.Text("История текстов:")
   
   def on_button_click(_):
      name = name_input.value.strip()
      age = age_input.value.strip()
      hour = datetime.now().hour 

     


      if 6 <= hour < 12:
         greenting = "good morning"
      elif 12 <= hour < 18:
         greenting = "good day"
      elif 18 <= hour < 24:
         greenting = "good evning"
      else:
         greenting = "good night"

      print(name)

      if name:
         print(greeting_text)
         greeting_text.value = f'{greenting} {name} {age} лет тебе'
         print(greeting_text)
         name_input.value =''
         age_input.value = ''

         greeting_history.append(f'{hour} - {name}')
         history_text.value = "История приветствий:\n" + "\n".join(greeting_history)


      else:
         print('не введино')
         greeting_text.value = 'пж введите имя'
      page.update()


   name_input = ft.TextField(label='Введите имя:', on_submit=on_button_click)
   age_input = ft.TextField(label='Введите возраст', on_submit=on_button_click)
   name_button = ft.ElevatedButton('send', on_click=on_button_click)


   def pop_history(_):
      if greeting_history:  
         greeting_history.pop()
         history_text.value = "история приветствий:\n" + "\n".join(greeting_history)
      
      else: 
         history_text.value = "История пуста!"

      page.update()

   pop_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=pop_history)
   
   page.add(greeting_text, name_input, age_input,
            ft.Row([name_button, pop_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            ft.Row([history_text], alignment=ft.MainAxisAlignment.START)
   )
ft.app(target=main)