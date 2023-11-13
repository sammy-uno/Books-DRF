# BOOKS API With DRF

<b>1. Admin Access</b>
<ul>
    <li>Admin Section: http://127.0.0.1:8000/dashboard/</li>
</ul>
<br>

<b>2. Accounts</b>
<ul>
    <li>Registration: http://127.0.0.1:8000/api/account/register/</li>
    <li>Login: http://127.0.0.1:8000/api/account/login/</li>
    <li>Logout: http://127.0.0.1:8000/api/account/logout/</li>
</ul>
<br>

<b>4. Book List</b>
<ul>
    <li>Create & Access List: http://127.0.0.1:8000/api/books/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/books/&lt;int:book_id&gt;/</li>
</ul>
<br>

<b>5. Reviews</b>
<ul>
    <li>Create Review For Specific Book: http://127.0.0.1:8000/api/books/&lt;int:book_id&gt;/reviews/create/</li>
    <li>List Of All Reviews For Specific Book: http://127.0.0.1:8000/api/book/&lt;int:book_id&gt;/reviews/</li>
    <li>Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/books/reviews/&lt;int:review_id&gt;/</li>
</ul>
<br>

<b>6. User Review</b>
<ul>
    <li>Access All Reviews For Specific User: http://127.0.0.1:8000/api/books/user-reviews/?username=example</li>
</ul>
<br>
