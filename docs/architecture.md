# Meta-Mühendislik Sistem Mimarisi

## Genel Bakış
Sistem, biyolojik metaforlar üzerine kurulmuş hibrit bir yapay zeka orkestrasyon motorudur.

## Bileşenler

### 1. Omni-Bus (Sinir Sistemi)
Tüm sistemin bel kemiğidir. Event-driven (Olay güdümlü) bir yapı sunar.
- **Publish/Subscribe Modeli:** Bileşenler birbirini tanımaz, sadece kanallara abone olur.
- **Asenkron İletişim:** Ajanlar bloklanmadan çalışır.

### 2. Ajan Sürüsü (Agent Swarm)
Özelleşmiş LLM tabanlı işçiler.
- **Architect:** Planlama ve üst seviye tasarım.
- **Coder:** Uygulama ve kod üretimi.
- **Reviewer:** Kalite kontrol ve güvenlik.

### 3. Hafıza Izgarası (Memory Grid)
- **Kısa Süreli Hafıza:** Python dictionary tabanlı, RAM üzerinde yaşayan, process ömrüyle sınırlı hafıza.
- **Uzun Süreli Hafıza:** Vektör tabanlı semantik hafıza simülasyonu.

### 4. Plugin Sistemi
Dışarıdan kod yüklemeye izin veren dinamik genişleme katmanı. `plugins/` klasörüne atılan `.py` dosyalarını otomatik tarar ve yükler.

## Veri Akışı
1. **Niyet (Intent):** Kullanıcıdan gelir.
2. **Planlama:** Architect niyeti parçalar.
3. **Dağıtım:** Planlar Omni-Bus üzerinden Coder'a gider.
4. **Üretim:** Coder kodu yazar ve Reviewer'a gönderir.
5. **Onay:** Reviewer onaylarsa kod sisteme entegre edilir.
