from flask import Flask, request, render_template_string, Response

app = Flask(__name__)

# HTML template with Element Plus time picker, Vue.js, and your provided HTML wrapper
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>t c h</title>
    <!-- Meta viewport for responsive design -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Element Plus CSS -->
    <link rel="stylesheet" href="https://unpkg.com/element-plus/dist/index.css">
    <link rel="icon" href="/static/tch.ico" type="image/x-icon">
    <style>
        /* Your existing styles */
        :root {
            /* Light mode */
            --background-color: #ffffff;
            --text-color: #000000;
            --link-color: #0d6efd; /* Bootstrap primary blue */
        }

        [data-theme="dark"] {
            /* Dark mode */
            --background-color: #121212;
            --text-color: #ffffff;
            --link-color: #81D4FA; /* Blue for links in dark mode */
        }

        body {
            font-family: Arial, sans-serif;
            background-color: var(--background-color);
            color: var(--text-color);
        }

        a {
            color: var(--link-color);
        }

        a:hover {
            text-decoration: underline;
        }

        .footer {
            background-color: rgba(0, 0, 0, 0.05);
        }

        [data-theme="dark"] .footer {
            background-color: rgba(255, 255, 255, 0.1);
        }

        [data-theme="dark"] .footer a.text-body {
            color: var(--link-color) !important;
        }

        #themeToggle {
            font-size: 12px; /* Smaller text size */
            padding: 5px 10px; /* Smaller button size */
        }

        .timecard-container {
            max-width: 500px;
            margin: 20px auto;
            padding: 20px;
            background: var(--background-color);
            border: 1px solid #dee2e6;
            border-radius: 8px;
            text-align: center;
        }

        .btn-primary {
            width: 100%;
        }

        .el-time-picker {
            width: 100%;
        }
    </style>
</head>
<body class="d-flex flex-column min-vh-100" data-theme="light">
    <div id="app" class="container flex-fill">
        <div class="text-center my-3">
            <a href="/"><img src="/static/tch.png" height="64" width="64" alt="tch logo"></a>
            <p class="h3 fw-bold">t c h</p>
            <div>
                <p><button id="themeToggle" class="btn btn-secondary">Toggle Dark Mode</button></p>
                <p>time card helper -- calculate the earliest moment you can clock out</p>
            </div>
        </div>
        <div class="text-center my-3">
            <div class="timecard-container">
                <form id="time-form" @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label for="timepicker" class="form-label">Clock-in Time (HH:MM)</label>
                        <div class="d-flex justify-content-center">
                            <!-- Conditionally render time picker based on device type -->
                            <div v-if="isMobile">
                                <input
                                    id="timepicker"
                                    name="time"
                                    type="time"
                                    v-model="time"
                                    class="form-control"
                                    style="max-width: 300px; width: 100%;"
                                    required
                                >
                            </div>
                            <div v-else>
                                <!-- Element Plus time picker with value-format -->
                                <el-time-picker
                                    v-model="time"
                                    format="HH:mm"
                                    value-format="HH:mm"
                                    placeholder="Select Time"
                                    :picker-options="{
                                        selectableRange: '00:00:00 - 23:59:59'
                                    }"
                                    style="max-width: 300px; width: 100%;"
                                ></el-time-picker>
                            </div>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary mt-3">Submit</button>
                </form>
                <div v-if="result" id="result" class="mt-4 alert alert-success">
                    Earliest clock-out: <strong>{{ result }}</strong>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer mt-auto py-3 text-center">
        <div class="container">
            <p class="mb-0">2024 by <a href="https://rickt.dev/" class="text-body">rickt</a></p>
        </div>
    </footer>

    <!-- Vue.js 3 (production build) -->
    <script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>
    <!-- Element Plus JS -->
    <script src="https://unpkg.com/element-plus"></script>
    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>

    <!-- Initialize Vue.js and Element Plus -->
    <script>
        const { createApp } = Vue;

        const app = createApp({
            data() {
                return {
                    time: {{ time_param | tojson }},  // Initialize with the submitted time
                    result: {{ result | tojson }},    // Result from Flask
                    isMobile: false                   // Flag to detect mobile devices
                }
            },
            methods: {
                submitForm() {
                    // Redirect to the Flask route with the time parameter
                    if (this.time) {
                        window.location.href = `/?time=${encodeURIComponent(this.time)}`;
                    } else {
                        alert('Please select a time.');
                    }
                }
            },
            mounted() {
                // Detect if the device is mobile
                this.isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            }
        });

        app.use(ElementPlus);
        app.mount('#app');

        // Dark mode toggle script
        const body = document.body;
        const themeToggle = document.getElementById('themeToggle');
        const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

        // Set theme based on device setting
        body.setAttribute("data-theme", prefersDarkScheme.matches ? "dark" : "light");

        // Listen for system theme changes
        prefersDarkScheme.addEventListener("change", (e) => {
            body.setAttribute("data-theme", e.matches ? "dark" : "light");
        });

        // Toggle theme manually
        themeToggle.addEventListener("click", () => {
            const currentTheme = body.getAttribute("data-theme");
            body.setAttribute("data-theme", currentTheme === "light" ? "dark" : "light");
        });
    </script>
</body>
</html>
"""

# adjust given time to the nearest main "timeband"
from datetime import datetime, timedelta
def get_timeband(time_str):
    time = datetime.strptime(time_str, "%H:%M")
    minutes = time.minute
    # obvious
    if minutes <= 7:
        time = time.replace(minute=0)
    elif 8 <= minutes <= 22:
        time = time.replace(minute=15)
    elif 23 <= minutes <= 37:
        time = time.replace(minute=30)
    elif 38 <= minutes <= 52:
        time = time.replace(minute=45)
    else:
        # 53min+ move to next hour
        time = (time + timedelta(hours=1)).replace(minute=0)
    return time

# return earliest possible time that fits within given time band
def get_timeband_start(time_band_time):
    # subtract 7min to get actual earliest time
    band_start = time_band_time - timedelta(minutes=7)
    return band_start

# calc earliest exact clock out time for a given time
def calculate_earliest_clock_out(clock_in):
    adjusted_clock_in = get_timeband(clock_in)
    required_work_time = timedelta(hours=8, minutes=30)
    adjusted_clock_out = adjusted_clock_in + required_work_time
    earliest_clock_out = get_timeband_start(adjusted_clock_out)
    return earliest_clock_out

# render page from template to get clock-in time so we can calculate earliest possible clock-out time
# if param mode=text specified, return plain text only
@app.route("/", methods=["GET"])
def timecard():
    time_param = request.args.get("time")
    mode = request.args.get("mode")
    result = None

    if time_param:
        try:
            datetime.strptime(time_param, "%H:%M")  # validate time format
            earliest_clock_out_dt = calculate_earliest_clock_out(time_param)
            # format to 12hr time w/am or pm
            formatted_time = earliest_clock_out_dt.strftime("%I:%M %p").lstrip('0').lower()
            result = formatted_time
        except ValueError:
            error_message = "Invalid time format. Use HH:MM."
            if mode == "text":
                return Response(error_message + "\n", content_type="text/plain")
            else:
                result = error_message
    else:
        time_param = ''
        if mode == "text":
            error_message = "No time parameter provided."
            return Response(error_message + "\n", content_type="text/plain")

    if mode == "text":
        # text only! return plain
        return Response(f"Earliest clock-out time: {result}\n", content_type="text/plain")
    else:
        # render the html
        return render_template_string(html_template, result=result, time_param=time_param)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
