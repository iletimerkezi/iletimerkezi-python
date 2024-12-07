# İleti Merkezi Python SDK

## Kurulum

Bu SDK'yı kullanmak için Python 3.7 veya daha üst bir sürümüne sahip olmalısınız. Aşağıdaki adımları izleyerek SDK'yı kurabilirsiniz:

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/iletimerkezi/iletimerkezi-python.git
   cd iletimerkezi-python
   ```

2. **Gerekli bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Alternatif olarak, doğrudan PyPI üzerinden yükleyebilirsiniz:**
   ```bash
   pip install iletimerkezi
   ```

## Kullanım

SDK'yı kullanmaya başlamak için aşağıdaki örneği inceleyebilirsiniz:

## İleti Merkezi istemcisini başlatın

```python
from iletimerkezi import IletiMerkeziClient

client = IletiMerkeziClient(
    api_key='YOUR_API_KEY',
    api_hash='YOUR_API_HASH',
    default_sender='YOUR_DEFAULT_SENDER'
)
```

### SMS Gönderme Örneği

```python
response = client.sms().send('5057023100', 'Merhaba Dünya!')
if response.ok():
    print("SMS başarıyla gönderildi! Sipariş ID:", response.order_id())
else:
    print(f"Hata: {response.get_error()}")
```


## Desteklenen Versiyonlar

Bu SDK, aşağıdaki Python sürümlerini desteklemektedir:

- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11

## İletişim

Herhangi bir sorun veya öneri için [destek@emarka.com.tr](mailto:destek@emarka.com.tr) adresiyle iletişime geçebilirsiniz.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.