# LvivBadStore

## About
Ecommerce website using Django.
Feel yourself like a hero on the court with clothes and equipment from our store.

## Installation
1. Clone this repository
    ```bash
    git clone https://github.com/SofiiaRomah/eCommerceShop.git
    ```
2. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
3. Create `.env` file in the project's root and define following variables inside
    ```bash
    DEBUG=
    SECRET_KEY=
    SOCIAL_AUTH_FACEBOOK_KEY=
    SOCIAL_AUTH_FACEBOOK_SECRET=
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=
    ```
4. Now you can run the development server
    ```bash
    python manage.py runserver_plus <address:port> --cert <filename>
    ```