# st.button

`st.button` แสดงปุ่มกดใน Streamlit

## เราจะสร้างอะไร?

แอปที่แสดงข้อความที่ไม่เหมือนกันขึ้นอยู่กับว่าปุ่มถูกกดหรือไม่

ขั้นตอนการทำงานของแอป

1. เมื่อโหลดแอปข้อความ `Goodbye` จะปรากฏขึ้น
2. เมื่อคลิกที่ปุ่มแอปจะแสดงข้อความที่สอง `Why hello there`

## แอปตัวอย่าง

แอปที่ถูก deploy บน Streamlit Community Cloud จะมีลักษณะที่แสดงในลิงก์ด้านล่างนี้

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## โค้ด

โค้ดสำหรับสร้างแอปที่กล่าวข้างต้น จะแสดงไว้ด้านล่างนี่

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## คำอธิบายทีละบรรทัด

สิ่งแรกที่ต้องทำเมื่อสร้างแอป Streamlit คือเริ่มด้วยการนำเข้าไลบรารี `streamlit` เป็น `st` ดังนี้

```python
import streamlit as st
```

ตามด้วยการสร้างข้อความส่วนที่จะเป็นหัว (header) ในแอป
```python
st.header('st.button')
```

หลังจากนั้นเราจะใช้รูปแบบคำสั่งกำหนดเงื่อนไข `if` และ `else` สำหรับพิมพ์ข้อความ

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

เราสามารถดูได้จากช่องโค้ดด้านบน คำสั่ง `st.button()` สามารถรับ `label` ที่มีค่า `Say hello` เป็นอินพุตสำหรับแสดงข้อความบนปุ่มกด

คำสั่ง `st.write` ใช้เพื่อพิมพ์ข้อความ `Why hello there` หรือ `Goodbye` ขึ้นอยู่กับว่าปุ่มนั้นถูกคลิกหรือไม่ ดังที่แสดงด้านล่างนี้


```python
st.write('Why hello there')
```

และ

```python
st.write('Goodbye')
```

เราสามารถสังเกตเห็นว่าข้อความ `st.write` ข้างต้นอยู่ภายใต้เงื่อนไข `if` และ `else` เพื่อแสดงข้อความหลักหรือข้อความทางเลือก

## ขั้นตอนถัดไป

ตอนนี้คุณก็สามารถสร้างแอป Streamlit บนเครื่องคอมพิวเตอร์ของคุณแล้ว ขั้นตอนต่อไปคือการ deploy แอปโดยใช้ [Streamlit Cloud](https://streamlit.io/cloud) ซึ่งจะอธิบายในบทเรียนต่อไป

เนื่องจากนี่เป็นสัปดาห์แรกของความท้าทายการเรียนรู้ เราจึงจัดเตรียมโค้ดทั้งหมด (ดังที่แสดงในช่องโค้ดด้านบน) และผลลัพธ์ (แอปตัวอย่าง) ไว้ในหน้าเว็บนี้

ในบทเรียนต่อไปขอแนะนำให้ผู้เรียนพยายามพัฒนาแอปโดยตัวท่านเอง

ไม่ต้องกังวลหากคุณติดขัด คุณสามารถดูวิธีแก้ปัญหาได้ตลอดเวลาจากแอปตัวอย่าง

## บทความอ้างอิง

คุณสามารถอ่านเกี่ยวกับ [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) จาก Streamlit API Documentation.
