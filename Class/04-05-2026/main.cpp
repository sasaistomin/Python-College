#include <iostream>
#include <vector>
#include <string>

class Herbivore {
protected:
    int weight;
    bool life;
    std::string name;

public:
    Herbivore(std::string n, int w) : name(n), weight(w), life(true) {}
    virtual ~Herbivore() {}

    void eat_grass() {
        if (life) {
            weight += 10;
        }
    }

    int get_weight() const { return weight; }
    bool is_alive() const { return life; }
    void die() { life = false; }
    std::string get_name() const { return name; }
};

class Carnivore {
protected:
    int power;
    std::string name;

public:
    Carnivore(std::string n, int p) : name(n), power(p) {}
    virtual ~Carnivore() {}

    void eat(Herbivore* victim) {
        if (!victim->is_alive()) return;

        if (this->power > victim->get_weight()) {
            power += 10;
            victim->die();
        } else {
            power -= 10;
        }
    }
};

class Wildebeest : public Herbivore {
public:
    Wildebeest() : Herbivore("Wildebeest", 50) {}
};

class Bison : public Herbivore {
public:
    Bison() : Herbivore("Bison", 100) {}
};

class Lion : public Carnivore {
public:
    Lion() : Carnivore("Lion", 70) {}
};

class Wolf : public Carnivore {
public:
    Wolf() : Carnivore("Wolf", 40) {}
};

class Continent {
public:
    virtual Herbivore* create_herbivore() = 0;
    virtual Carnivore* create_carnivore() = 0;
    virtual ~Continent() {}
};

class Africa : public Continent {
public:
    Herbivore* create_herbivore() override { return new Wildebeest(); }
    Carnivore* create_carnivore() override { return new Lion(); }
};

class NorthAmerica : public Continent {
public:
    Herbivore* create_herbivore() override { return new Bison(); }
    Carnivore* create_carnivore() override { return new Wolf(); }
};

class AnimalWorld {
private:
    std::vector<Herbivore*> herbivores;
    std::vector<Carnivore*> carnivores;

public:
    AnimalWorld(Continent* factory) {
        herbivores.push_back(factory->create_herbivore());
        carnivores.push_back(factory->create_carnivore());
    }

    ~AnimalWorld() {
        for (auto h : herbivores) delete h;
        for (auto c : carnivores) delete c;
    }

    void meals_herbivores() {
        for (auto h : herbivores) h->eat_grass();
    }

    void nutrition_carnivores() {
        for (auto c : carnivores) {
            for (auto h : herbivores) {
                if (h->is_alive()) c->eat(h);
            }
        }
    }
};

int main() {
    Continent* africaFactory = new Africa();
    AnimalWorld* africaWorld = new AnimalWorld(africaFactory);
    africaWorld->meals_herbivores();
    africaWorld->nutrition_carnivores();

    Continent* naFactory = new NorthAmerica();
    AnimalWorld* naWorld = new AnimalWorld(naFactory);
    naWorld->meals_herbivores();
    naWorld->nutrition_carnivores();

    delete africaWorld; delete africaFactory;
    delete naWorld; delete naFactory;

    return 0;
}