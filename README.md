## Скрипт list_notebooks.py

Программа отображает список блокнотов с их идентификаторами.  

### Как запускать
```console
foo@bar:~$ python list_notebooks.py
```

## Скрипт add_note2journal.py

Программа добавляет заметку в "Дневник", используя шаблон заметки.  

### Как запускать
```console
foo@bar:~$ python add_note2journal.py [date]
```
где `date` - дата в дневнике, в формате "YYYY-MM-DD".

## Скрипт dump_inbox.py

Программа отображает список заметок из блокнота.  

### Как запускать

```console
foo@bar:~$ python dump_inbox.py [number]
```
где `number` - количество выводимых заметок.


--------------------------------------------------------------------------------
## Первоначальная настройка
Python2 должен быть уже установлен.  
Скопируйте файл `.env.Example` и переименуйте его в `.env`.  

Заполните переменные окружения:  
`EVERNOTE_PERSONAL_TOKEN` - TOKEN от API Evernot.  
`JOURNAL_TEMPLATE_NOTE_GUID` - Идентификатор шаблона заметки.  
`JOURNAL_NOTEBOOK_GUID` - Идентификатор "Дневника".  
`INBOX_NOTEBOOK_GUID` - Идентификатор блокнота.  
`SANDBOX` - Если необходимо протестировать скрипты в "песочнице", установите значение в `True`.  
