![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
## Как удалить файлы случайно добавленные в гит? ##

На примере папки .idea

- $ echo '.idea' >> .gitignore

- $ git rm -r --cached .idea

- $ git add .gitignore

- $ git commit -m '(some message stating you added .idea to ignored entries)'

- $ git push

![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)