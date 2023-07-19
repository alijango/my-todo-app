mkdir -p ~/.streamlit/

echo "\
[general]\n\
<<<<<<< HEAD
email = \"alielali.py@gmail.com\"\n\
=======
email = \"alialali_a@hotmail.com\"\n\
>>>>>>> a073f5f (Add configuration files)
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml