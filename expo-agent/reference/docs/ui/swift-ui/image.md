---
title: "Image"
description: "A SwiftUI Image component for displaying SF Symbols."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/image.md"
scraped_at: "2026-07-15T08:59:10.374941"
---

---
title: Image
description: A SwiftUI Image component for displaying SF Symbols.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Image

A SwiftUI Image component for displaying SF Symbols.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Icon`](/versions/latest/sdk/ui/universal/icon.md) — it renders the appropriate native component per platform.

Expo UI Image displays SF Symbols using the SwiftUI [Image API](https://developer.apple.com/documentation/swiftui/image). SF Symbols are a library of configurable symbols provided by Apple.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic SF Symbol

```tsx
import { Host, Image } from '@expo/ui/swift-ui';

export default function BasicImageExample() {
  return (
    <Host matchContents>
      <Image systemName="star.fill" />
    </Host>
  );
}
```

### Custom SF Symbol

Use the `assetName` prop to display a custom SF Symbol imported into the app asset catalog as a symbol set.

```tsx
import { Host, Image } from '@expo/ui/swift-ui';

export default function CustomImageExample() {
  return (
    <Host matchContents>
      <Image assetName="acme.mark" />
    </Host>
  );
}
```

### With size and color

```tsx
import { Host, HStack, Image } from '@expo/ui/swift-ui';

export default function ImageSizeColorExample() {
  return (
    <Host matchContents>
      <HStack spacing={16}>
        <Image systemName="heart.fill" size={24} color="red" />
        <Image systemName="star.fill" size={32} color="orange" />
        <Image systemName="bell.fill" size={40} color="blue" />
      </HStack>
    </Host>
  );
}
```

### With variable value

Some SF Symbols alter their appearance based on a variable value. Use the `variableValue` prop with a value between 0.0 and 1.0 to control the rendered symbol. Requires iOS 16.0+ and SF Symbols 4.0+.

```tsx
import { Host, HStack, Image } from '@expo/ui/swift-ui';

export default function ImageVariableExample() {
  return (
    <Host matchContents>
      <HStack spacing={16}>
        <Image systemName="chart.bar.fill" size={32} variableValue={0.3} />
        <Image systemName="chart.bar.fill" size={32} variableValue={0.6} />
        <Image systemName="chart.bar.fill" size={32} variableValue={1.0} />
      </HStack>
    </Host>
  );
}
```

### With symbol effect

Apply an SF Symbol effect to animate the symbol by passing a [`symbolEffect`](/versions/latest/sdk/ui/swift-ui/modifiers.md#symboleffecteffect-args) modifier from `@expo/ui/swift-ui/modifiers`. This effect runs continuously by default. You can also pass `value` for a discrete trigger that fires once per change, or `isActive` for a boolean toggle that runs the effect while `true`. Requires iOS 17.0 and later.

```tsx
import { Host, Image } from '@expo/ui/swift-ui';
import { symbolEffect } from '@expo/ui/swift-ui/modifiers';

export default function ImageSymbolEffectExample() {
  return (
    <Host matchContents>
      <Image
        systemName="wifi"
        size={48}
        color="blue"
        modifiers={[
          symbolEffect({
            effect: 'variableColor',
            fillStyle: 'iterative',
            playbackStyle: 'reversing',
          }),
        ]}
      />
    </Host>
  );
}
```

The following example uses `value` to play `bounce` on each button press. Write to `state.value` from a worklet (or via [`scheduleOnUI`](https://docs.swmansion.com/react-native-worklets/docs/threading/scheduleOnUI)) to trigger the effect.

```tsx
import { Button, Host, Image, useNativeState, VStack } from '@expo/ui/swift-ui';
import { symbolEffect } from '@expo/ui/swift-ui/modifiers';
import { scheduleOnUI } from 'react-native-worklets';

export default function ImageSymbolEffectValueExample() {
  const trigger = useNativeState(0);

  return (
    <Host matchContents>
      <VStack spacing={16}>
        <Image
          systemName="bell.fill"
          size={48}
          color="orange"
          modifiers={[symbolEffect({ effect: 'bounce', direction: 'up' }, { value: trigger })]}
        />
        <Button
          label="Bounce"
          onPress={() =>
            scheduleOnUI(() => {
              'worklet';
              trigger.value = trigger.value + 1;
            })
          }
        />
      </VStack>
    </Host>
  );
}
```

The following example uses `isActive` to toggle a continuous `breathe` animation.

```tsx
import { Host, Image, SyncToggle, useNativeState, VStack } from '@expo/ui/swift-ui';
import { symbolEffect } from '@expo/ui/swift-ui/modifiers';

export default function ImageSymbolEffectIsActiveExample() {
  const isActive = useNativeState(true);

  return (
    <Host matchContents>
      <VStack spacing={16}>
        <Image
          systemName="cloud.fill"
          size={48}
          color="cyan"
          modifiers={[symbolEffect({ effect: 'breathe' }, { isActive })]}
        />
        <SyncToggle label="Breathe" isOn={isActive} />
      </VStack>
    </Host>
  );
}
```

## API

```tsx
import { Image } from '@expo/ui/swift-ui';
```

## Component

### `Image`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ImageProps](#imageprops)\>

ImageProps

### `assetName`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

The asset catalog name of a custom SF Symbol imported as a symbol set.

### `color`

Supported platforms: iOS, tvOS.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the system image. Can be a color name like '#ff00ff', 'red', 'blue', etc.

### `onPress`

Supported platforms: iOS, tvOS.

Optional • Type: `() => void`

Callback triggered when the view is pressed.

### `size`

Supported platforms: iOS, tvOS.

Optional • Type: `number`

The fixed size of the system image in points. Does not scale with Dynamic Type. Use the `font` modifier with `textStyle` for that. Ignored when a `font` modifier is supplied.

### `systemName`

Supported platforms: iOS, tvOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

The name of the system image (SF Symbol). For example: 'photo', 'heart.fill', 'star.circle'

### `uiImage`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

The URI of the local image file to display. For example: 'file:///path/to/image.jpg' Performs a synchronous read operation that blocks the main thread.

### `variableValue`

Supported platforms: iOS16.0+, tvOS16.0+.

Optional • Type: `number`

The variable value that alters the symbol's appearance. A number between 0.0 and 1.0. Only works with SF Symbols that support variable values (SF Symbols 4.0+).

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
