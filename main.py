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
      

     

      print(name)

      if name:
         print(greeting_text)
         greeting_text.value = f'HELLO {name} '
         print(greeting_text)
         name_input.value =''
         timestamp = datetime.now().strftime('%Y:%S')
      

         greeting_history.append(f'{timestamp} - {name}')
         history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
         


      else:
         print('не введино')
         greeting_text.value = 'пж введите имя'
      page.update()


   name_input = ft.TextField(label='Введите имя:', on_submit=on_button_click)
   name_button = ft.ElevatedButton('send', on_click=on_button_click)

   def clear_history(_):
      greeting_history.clear()
      history_text.value = 'история приветствий:'
      page.update()

   clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
   
   #page.add(greeting_text, name_input, name_button, clear_button, history_text)

   page.add(greeting_text, name_input,
            ft.Row([name_button, clear_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            ft.Row([history_text], alignment=ft.MainAxisAlignment.START)
            )

ft.app(target=main)


