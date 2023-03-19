# Super Silly Security

| Difficulty | Points |
| ---------- | ------ |
| Easy       | 500    |


## Description

> The vikings have founded a new venture, BaaS (Battleaxes-as-a-Service). Their
> promise of secure storage is enticing, but this is the cloud...is it actually
> secure?
> <details>
> <summary>Hint 1</summary>
> What cloud service provides simple storage of static sites?
> </details>
> <details>
> <summary>Hint 2</summary>
> That error seems specific, what's <code>Authenticated AWS User group</code>?
> </details>

## Approach

Flag: 

The given website has an image named `flag.png` containing an S3 error message.

We then tried to use the AWS CLI configured with a valid AWS Access Key and
Secret Access Key to list the contents of the S3 bucket.

```
aws s3 ls s3://<bucket-name>
```

This listed some files including the `flag.png` from the website.

```
aws s3 cp s3://<bucket-name>/flag.png ./flag.png
```

this image contains the flag:

![Image of flag](./flag.png)

Flag:

```
vikeCTF{c@r3fu1_w!7h_@cc355_c0n7r01$}
```
