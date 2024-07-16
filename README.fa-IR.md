[![en](https://img.shields.io/badge/lang-en-red.svg) ENGLISH](https://github.com/mer30hamid/v2rayN-Routing-Rules-Generator/blob/main/README.md)

<div dir="rtl">
# اسکریپت مولد پیکربندی من برای v2rayN

یک اسکریپت پایتون که قوانین مسیریابی را با فرمت json برای برنامه [v2rayN برنامه](https://github.com/2dust/v2rayN) ایجاد می‌کند.

## ویژگی ها:
   * "لیست بلاک" برای لینک های بد پارسی (https://github.com/MasterKia/PersianBlocker/)
   * لیست سفید برای سایت های پارسی (https://github.com/SamadiPour/iran-hosted-domains/)
   * نگهداری لیست بلاک در حافظه موقت و همچنین کنترل زمان  اعتبار ماندگاری حافظه موقت (کش)

## وابستگی ها:
  * پایتون 3 (https://www.python.org/downloads)
  * نیازمندی های پایتون:
    * requests

## تولید پیکربندی:
  * در صورتی که بار اول اسکریپت را اجرا می کنید:
    * نیازمندی های پایتون را با این دستور نصب کنید:`pip install -r requirements.txt`
  * اسکریپت را با استفاده از پایتون اجرا کنید:`python generate-rules.py` این دستور یک فایل با نام `v2rayN_rules.json` ایجاد می کند.

## روش های استفاده
### روش اول: وارد کردن قوانین مسیریابی توسط آدرس ساب (اشتراک)

1.  آدرس زیر را کپی کنید:
``` 
  https://raw.githubusercontent.com/mer30hamid/v2rayN-Routing-Rules-Generator/main/v2rayN_rules.json
```
  و در این مسیر قرار دهید:
     
  **Settings -> RoutingSetting -> Advanced Function -> Add -> URL(Optional)**
     
>**نکته: می توانید روی سرور خودتان اسکریپت را اجرا و فایل تولید شده را میزبانی کنید ولی این آدرس هر روز توسط اکشن های گیتهاب، بصورت خودکار بروز می شود!**

2. یک نام قرار دهید (در قسمت Remarks مثلا بگذارید "Iran")
3. روی دکمه "Import Rules From Subscription URL" کلیک کنید
4. وقتی پرسید "do you want to append rules? ..." دکمه `yes` را بزند.
5. روی "Confirm" کلیک کنید تا قوانین ذخیره شوند.

  ![image](https://github.com/user-attachments/assets/cbbe22dc-4143-4e04-a161-2351d4eb433a)

6. پایین نرم افزار (در قسمت routing), آن را انتخاب کنید (Iran)

  ![image](https://github.com/user-attachments/assets/a38613e9-2126-429c-a22e-000a877dcced)


​     

### روش دوم: وارد کردن قوانین از طریق باز کردن فایل
1. به این مسیر بروید:

**Settings -> RoutingSetting -> Advanced Function -> Add**

  
  و یک نام برای آن بگذارید (در قسمت Remarks مثلا بگذارید "Iran-local")

2. روی "Import Rules from file" کلیک کنید و فایلی که تولید کردید (یا دانلود کردید) با نام "v2rayN_rules.json" را انتخاب کنید.
3. روی "yes" و سپس "Confirm" کلیک کنید تا قوانین ذخیره شوند.

  ![image](https://github.com/user-attachments/assets/69309327-4a4a-440b-a4b0-8c23bd7331bd)

4. پایین نرم افزار (در قسمت routing), آن را انتخاب کنید (Iran-local)

  ![image](https://github.com/user-attachments/assets/a38613e9-2126-429c-a22e-000a877dcced)


</div>
