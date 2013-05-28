# Shadow Password Crypt

This is a short python script that accepts a password and generates a crypt(3)
sha512 password hash for use with useradd(8). This is the hash format used
by /etc/shadow.

## Usage

```bash
python shadow_password_crypt.py
```

## Example Output

```bash
$ python shadow_password_crypt.py
Password:
Confirm:
$6$kqWvIApH$zJVTydg7UO4VekhXjnblLOtBbWmzFuKyjHv54MjeOZ0k8YocSeiXtdg0x5l/jZKLBNFNpbFB0Pv6OhZVv3RD81
```
