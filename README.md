# Описание
Скрипт на `Python`, который парсит вывод от сетевого устройства и заполняет объекты, описывающие интерфейсы.

# Запуск
```commandline
python src/main.py -i PATH_TO_NETWORK_DEVICE_OUTPUT_FILE_TXT -o PATH_TO_RESULT_FILE_XML
```
- `PATH_TO_NETWORK_DEVICE_OUTPUT_FILE_TXT` - Файл с выводом сетевого устройства в формате `.txt`
- `PATH_TO_RESULT_FILE_XML` - Файл с полученными сетевыми настройками сетевого устройства в формате `.xml`

## Функциональные требования

- Есть вывод от сетевого устройства в виде многострочного текста.
- Создаются объекты, которые описывают модель настроек, парсится вывод и заполняются эти объекты.
- Сериализовываются объекты в XML.
- Запуск скрипта не требует сторонних библиотек.

## Модульные тесты

Для проверки работы программы, написаны модельные тесты, которые проверяют корректность парсинга, создания объектов и сериализации.

## Пример входных данных

 Выше и ниже полезной нагрузки могут быть строки с пояснительными данными, которые должны игнорироваться.

```
Flags: X - disabled, R - running; S - slave
 0 RS ;;; LAN
      name="LAN" default-name="ether2" mtu=1500 mac-address=50:00:00:31:00:01 orig-mac-address=50:00:00:31:00:01 arp=enabled arp-timeout=auto loop-protect=on loop-protect-status=on
      loop-protect-send-interval=5s loop-protect-disable-time=5m disable-running-check=yes auto-negotiation=yes advertise=10M-half,10M-full,100M-half,100M-full,1000M-full full-duplex=yes
      tx-flow-control=off rx-flow-control=off cable-settings=default speed=1Gbps bandwidth=unlimited/unlimited
 
 1 R  name="ether1" default-name="ether1" mtu=1500 mac-address=50:00:00:31:00:00 orig-mac-address=50:00:00:31:00:00 arp=enabled arp-timeout=auto loop-protect=default loop-protect-status=off
      loop-protect-send-interval=5s loop-protect-disable-time=5m disable-running-check=yes auto-negotiation=yes advertise=10M-half,10M-full,100M-half,100M-full,1000M-full full-duplex=yes
      tx-flow-control=off rx-flow-control=off cable-settings=default speed=1Gbps bandwidth=unlimited/unlimited
 
 2 RS name="ether3" default-name="ether3" mtu=1500 mac-address=50:00:00:31:00:02 orig-mac-address=50:00:00:31:00:02 arp=proxy-arp arp-timeout=auto loop-protect=default loop-protect-status=off
      loop-protect-send-interval=5s loop-protect-disable-time=5m disable-running-check=yes auto-negotiation=yes advertise=10M-half,10M-full,100M-half,100M-full,1000M-full full-duplex=yes
      tx-flow-control=off rx-flow-control=off cable-settings=default speed=1Gbps bandwidth=unlimited/unlimited
 
 3 X  ;;; bla bla description for the ether4 interface
      name="ether4" default-name="ether4" mtu=1500 mac-address=50:00:00:31:00:03 orig-mac-address=50:00:00:31:00:03 arp=enabled arp-timeout=auto loop-protect=default loop-protect-status=off
      loop-protect-send-interval=5s loop-protect-disable-time=5m disable-running-check=yes auto-negotiation=yes advertise=10M-half,10M-full,100M-half,100M-full,1000M-full full-duplex=yes
      tx-flow-control=off rx-flow-control=off cable-settings=default speed=1Gbps bandwidth=unlimited/unlimited
```
## Требования к модели

Модель должна быть представлена классом Python с набором атрибутов:

* Id – берется из `name=`
* Name – берется из `default-name=`
* Description – берется из строки с порядковым номером и после паттерна `;;;`, если есть.
* MacAddress – берется из `mac-address=`
* Status – берется из флагов X, R, S. Если R – то записать значение "up". В остальных случаях – "down".
