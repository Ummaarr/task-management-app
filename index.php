<?php
$json = file_get_contents('http://127.0.0.1:5000/tasks'); // Fetch tasks from Flask backend
$tasks = json_decode($json, true); // Decode JSON response to PHP array
?>
<html>
<head>
    <title>Task Management</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h2 class="mt-4">Task List</h2>
        <ul class="list-group">
            <?php if (!empty($tasks)): ?>
                <?php foreach ($tasks as $task): ?>
                    <li class="list-group-item">
                        <strong><?php echo $task['title']; ?></strong><br>
                        <?php echo $task['description']; ?>
                    </li>
                <?php endforeach; ?>
            <?php else: ?>
                <li class="list-group-item">No tasks available</li>
            <?php endif; ?>
        </ul>
    </div>
</body>
</html>
