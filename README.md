## Gestor de contraseñas S-PASS 

S-PASS és un gestor de contrasenyes segur dissenyat per proporcionar un emmagatzematge i gestió eficients de les contrasenyes en un entorn digital cada vegada més complex. Desenvolupat en el context d'un curs d'estudis de Ciberseguretat, S-PASS aborda la necessitat crítica de gestionar contrasenyes de manera segura i efectiva, oferint una solució integral tant per a usuaris individuals com empresarials.

![GIF cyber](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmZxaGVqNmVlMzJoeTM5NjdvZnFyeXVwb21vdmhvOXU2N3p1dmt6biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RDZo7znAdn2u7sAcWH/giphy.gif)


## Característiques

- **Generació de Contrasenyes Segures**: Permet crear contrasenyes robustes i úniques que incrementen la seguretat de les teves comptes.
- **Emmagatzematge Segur**: Totes les contrasenyes es guarden en una base de dades xifrada, protegint la informació contra accessos no autoritzats.
- **Interfície Intuïtiva**: Dissenyada per ser fàcil d'usar, facilitant la gestió de contrasenyes per a tots els usuaris, independentment del seu nivell tecnològic.
- **Autenticació de Dos Factors (2FA)**: Afegeix una capa extra de seguretat verificant la teva identitat mitjançant dos mètodes diferents.


S-PASS és un gestor de contrasenyes dissenyat per integrar-se de forma natural en la vida quotidiana dels usuaris. Segons paraules de Eduard Bantulà, una expert en ciberseguretat i usuari habitual de S-PASS:

> "L'objectiu principal de disseny de S-PASS és oferir 
una gestió de contrasenyes tan intuïtiva com segura.
> La idea és que qualsevol persona pugui utilitzar S-PASS
> per gestionar les seves contrasenyes de manera eficient, 
sense necessitat de tenir coneixements tècnics.
> El gestor s'encarrega de tot, i la gestió de contrasenyes 
és tan senzilla i transparent que els usuaris ni tan sols 
noten que estan emprant mesures de seguretat avançades."

## Instal·lació
Per executar S-PASS localment, necessites tenir Python i Django instal·lats al teu sistema. Aquí tens els passos per configurar el projecte:

```sh
git clone https://github.com/tu-usuario/s-pass.git
cd s-pass
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


Per instal·lar i desplegar S-PASS en un contenidor Docker, segueix aquests passos:
```sh
cd s-pass
docker build -t tu-usuario/s-pass .
docker run -d -p 8000:8000 tu-usuario/s-pass
```

Llicència
MIT

Free Software, Hell Yeah!


![Logo de OpenAI](https://static.wikia.nocookie.net/marisqueria/images/1/19/Donpollo.jpeg/revision/latest?cb=20230105232639&path-prefix=es)
