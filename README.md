# ifj23-testutility
testy návratových kódu v projektu ifj23

test.py zavolá make a potom program ./main postupně spouští s kódy ze složky /test/ jakýkoli soubor ve složce se spustí nebo přeskočí.

očekávaný návratový kód je v příponě.
  .ok -> návratový kód 0
  .e[1-9] -> návratový kód 1 - 9  příklad .e1 -> chyba lexeru

přidávání vlastních testů:
  jednoduše přidejte soubor s kóde s příslušnou příponou do složky test.


!pozor test.py musí být ve stejné složce jako make a ./main a složka test musí být ve stejném adresáři
  


