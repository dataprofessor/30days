# st.button

`st.button` แสดงปุ่มกดใน Streamlit

## เราจะสร้างอะไร?

แอปที่แสดงข้อความที่ไม่เหมือนกันขึ้นอยู่กับว่าปุ่มถูกกดหรือไม่

ขั้นตอนการทำงานของแอป

1. เมื่อโหลดแอปข้อความ `Goodbye` จะปรากฏขึ้น
2. เมื่อคลิกที่ปุ่มแอปจะแสดงข้อความที่สอง `Why hello there`

## Demo app

แอปที่ถูก deploy บน Streamlit Community Cloud จะมีลักษณะเช่นในลิงก์ด้านล่างนี้

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Code

Here's the code to implement the above mentioned app:

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## Line-by-line explanation

The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:

```python
import streamlit as st
```

This is followed by creating a header text for the app:

```python
st.header('st.button')
```

Next, we will use conditional statements `if` and `else` for printing alternative messages.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

As we can see from the above code box, the `st.button()` command accepts the `label` input argument of `Say hello`, which is the text that the button displays.

The `st.write` command is used to print text messages of either `Why hello there` or `Goodbye` depending on whether the button was clicked or not, which is implemented via:


```python
st.write('Why hello there')
```

and

```python
st.write('Goodbye')
```

It is important to note that the above `st.write` statements are placed under the `if` and `else` conditions in order to perform the above mentioned process of alternative displaying of messages

## Next steps

Now that you have created the Streamlit app locally, it's time to deploy it to [Streamlit Cloud](https://streamlit.io/cloud) as will be explained soon in an upcoming challenge.

Because this is the first week of your challenge, we provide the full code (as shown in the code box above) and solution (the demo app) right inside this webpage.

Moving forward in the next challenges, it is recommended that you first try implementing the Streamlit app yourself.

Don't worry if you get stuck, you can always take a peek at the solution.

## References

Read about [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) in the Streamlit API Documentation.
