schema Resource:
    cpu: int
    memory: str

schema Config:
    resource: Resource

r = Resource {
    cpu = 4
    memory = "8Gi"
}

config: Config {
    resource: {**r}
}

config: Config {
    resource: Resource {
        cpu = 2
        memory = "4Gi"
    }
}
