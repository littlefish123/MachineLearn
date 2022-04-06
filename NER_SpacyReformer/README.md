Setup Spacy - Transformer Model
===============================
(1)
install rust compiler by running "rust computer/rustup-init.exe"
edit PATH env variable %USERPROFILE%\.cargo\bin

(2)
install visual C++ Build Tools  (Vs 2019 option installed)
Select "MSVC v142 - VS 2019 C++ x64/x86 build tools" and "Windows 10 SDK"

(3)
pip install --upgrade pip
pip install -U pip setuptools wheel
pip install -U "spacy[transformers,lookups]"
python -m spacy download zh_core_web_trf
python -m spacy download en_core_web_trf

(3.5)
python -m spacy init fill-config base_config.cfg configs\config.cfg

(4) 
python scripts/convert.py en assets/train.json corpus/train.spacy
python scripts/convert.py en assets/dev.json corpus/dev.spacy

(5) 
python -m spacy train configs/config.cfg --output training/ --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy --training.eval_frequency 10 --training.max_steps 100 --gpu-id -1
