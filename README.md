# todo_list

todo list

## Deployment notes

When deploying to a platform such as Render the application must know which
hostnames are allowed by Django. The settings file reads the
`ALLOWED_HOSTS` environment variable (comma-separated) and also automatically
whitelists the host provided by Render via `RENDER_EXTERNAL_URL`.

Make sure to set `ALLOWED_HOSTS` in your environment or rely on the above
fallback to avoid `DisallowedHost` errors. If the variable is omitted the
settings file will automatically log a warning and allow all hosts (i.e. the
`['*']` wildcard) so the service can still respond on the dynamically
allocated Render URL — but you should not rely on that in a real
production deployment.

For local development you can run:

```bash
export ALLOWED_HOSTS=localhost,127.0.0.1
```

Other platforms may require similar configuration.
