<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>todo-list README</title>
  <style>
    body {
      background-color: #1e1e1e;
      color: #e0e0e0;
      font-family: 'Segoe UI', sans-serif;
      padding: 2rem;
      line-height: 1.7;
    }
    h1, h2, h3 {
      color: #fff;
      margin-top: 2rem;
    }
    code {
      background-color: #333;
      color: #0ff;
      padding: 0.2rem 0.4rem;
      border-radius: 4px;
      font-size: 0.95em;
    }
    pre {
      background-color: #121212;
      padding: 1rem;
      border-radius: 8px;
      overflow-x: auto;
      border: 1px solid #333;
    }
    blockquote {
      border-left: 4px solid #666;
      padding-left: 1rem;
      color: #ccc;
      margin: 1rem 0;
      font-style: italic;
    }
    a {
      color: #0af;
      text-decoration: none;
    }
    hr {
      border: none;
      border-top: 1px solid #444;
      margin: 2rem 0;
    }
  </style>
</head>
<body>

  <h2>📋 TO-DO LIST MENU</h2>
  <pre><code>
=== TO-DO LIST MENU ===
1. Add
2. View
3. Complete
4. Delete
5. Quit
  </code></pre>

  <h2>📸 Sneak Peek</h2>
  <blockquote>“If it's not terminal, it’s not real.” – Me, probably.</blockquote>
  <pre><code>1 -&gt; Finish CS50P
2 -&gt; Write README like a boss
3 -&gt; Push to GitHub
  </code></pre>

  <h2>🧠 Logic Overview</h2>
  <ul>
    <li><code>tasks</code>: stores active to-dos.</li>
    <li><code>completed</code>: keeps your trophy shelf.</li>
    <li>Structured into functions:
      <ul>
        <li><code>add_task()</code></li>
        <li><code>view_tasks()</code></li>
        <li><code>complete_task()</code></li>
        <li><code>delete_task()</code></li>
      </ul>
    </li>
  </ul>

  <h2>💡 Why?</h2>
  <p>Because productivity apps are cool until they nag you with notifications.</p>
  <p>This one just sits quietly and listens — like a good terminal <s>friend</s>.</p>

  <h2>❤️ Author</h2>
  <p>Built with caffeine, dark mode, and Python by <a href="https://github.com/arjun05-tf" target="_blank">@arjun05-tf</a></p>

</body>
</html>
