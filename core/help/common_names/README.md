# Avoid private names leaking

It is very important that when you add personal names to the
`private_first_names.csv` and `private_last_names.csv` file, that you update
your git repository to stop tracking the files, to ensure that your information
is not accidentally pushed into a public repo. this can be done with the
following command:

```
git update-index --assume-unchanged <path to private_first_names.csv>
```
