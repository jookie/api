// npm install python-shell

const { PythonShell } = require('python-shell');

export default function handler(req, res) {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'],
        scriptPath: './', // path to your python script
        args: [] // any arguments to pass
    };

    PythonShell.run('buy_apple.py', options, function (err, results) {
        if (err) {
            res.status(500).json({ error: err.toString() });
        } else {
            res.status(200).json({ results });
        }
    });
}
