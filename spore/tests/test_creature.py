from spore.creature import CreatureBuilder, Evolution, GeneratorFromSequence, Creature


def test_distance_until_exhausted_with_regular_builder() -> None:
    builder = CreatureBuilder()
    builder.with_speed(5)
    builder.with_stamina(20)
    creature = builder.build()

    assert creature.distance_until_exhausted() == 100


def test_distance_until_exhausted_with_fluent_builder() -> None:
    creature = CreatureBuilder().with_speed(5).and_stamina(20).build()

    assert creature.distance_until_exhausted() == 100


def test_evolution() -> None:
    builder = CreatureBuilder()
    evolution = Evolution(builder, GeneratorFromSequence(n for n in [1, 2, 3, 4]))

    evolution.evolve()

    assert builder.build() == Creature(speed=1, stamina=2, power=3, health=4)

# Let's try to extract Speed class with method .distance(using=stamina)
# How will that change our tests? builder? Evolution?
