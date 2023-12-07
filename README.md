<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InfernBot - Django Telegram Bot Integration</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 20px;
            padding: 20px;
        }

        h1 {
            color: #007BFF;
        }

        h2 {
            color: #6610F2;
        }

        p {
            color: #6C757D;
        }

        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 4px;
        }

        pre {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        .installation {
            background-color: #28A745;
            color: #fff;
            padding: 10px;
            border-radius: 6px;
            margin-top: 20px;
        }
    </style>
</head>

<body>

    <div class="container">
        <header>
            <h1>InfernBot - Django Telegram Bot Integration</h1>
        </header>

        <main>
            <section>
                <h2>Overview</h2>
                <p>
                    InfernBot is a Django project that seamlessly combines the power of Django, Django Rest Framework, and
                    PyTelegramBotApi to create a versatile Telegram bot capable of handling notes and more.
                </p>
            </section>

            <section>
                <h2>Features</h2>
                <ul>
                    <li><strong>Note Creation:</strong> InfernBot allows users to create and manage notes through a Telegram
                        interface.</li>
                    <li><strong>Educational Example:</strong> Originally developed as an educational resource, this project
                        serves as a great example of integrating Django and Telegram Bot functionalities.</li>
                </ul>
            </section>

            <section class="installation">
                <h2>Getting Started</h2>
                <pre>
<code>
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Run the Django admin site
python3 manage.py runserver

# Start the Telegram bot
python3 manage.py runtgbot
</code>
                </pre>
            </section>
        </main>

        <footer>
            <a href="https://instagram.com/marselle.naz">Marselle.naz</a>
            <p>&copy; 2023 InfernBot. All rights reserved.</p>
        </footer>
    </div>

</body>

</html>
