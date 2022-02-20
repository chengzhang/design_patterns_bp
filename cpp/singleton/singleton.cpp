class Singleton {
protected:
    Singleton(const std::string value): value_(value) {}

    static Singleton* instance_;
    std::string value_;

public:
    Singleton(Singleton &other) = delete;
    void operator=(const Singleton &) = delete;
    static Singleton* GetInstance(const std::string& value) {
        if (instance_ == nullptr) {
            instance_ = new Singleton(value)
        }
        return instance_;
    }

    std::string value() const {
        return value_;
    }
    void whoami() {
        std::cout << "id: " << this << ", value: " << value_ << std::endl;
    }
    void some_business_logic() {}
};

Singleton* Singleton::singleton_ = nullptr;;

int main() {
    a = Singleton::GetInstance("foo")
    b = Singleton::GetInstance("bar")
    a.whoami()
    b.whoami()
    return 0;
}
