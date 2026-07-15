---
title: "FieldGroup"
description: "A scrollable container of grouped settings-style rows."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/fieldgroup.md"
scraped_at: "2026-07-15T09:01:47.906753"
---

---
title: FieldGroup
description: A scrollable container of grouped settings-style rows.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# FieldGroup

A scrollable container of grouped settings-style rows.
Android, iOS, Web, Included in Expo Go

A scrollable container for grouped settings-style rows, mirroring the look of an iOS Settings screen. Compose `FieldGroup.Section` (for explicit groups), `FieldGroup.SectionHeader`, and `FieldGroup.SectionFooter` slots inside.

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

### Sectioned form

```tsx
import { useState } from 'react';
import { Host, FieldGroup, Switch, Text } from '@expo/ui';

export default function FieldGroupExample() {
  const [notifications, setNotifications] = useState(true);
  const [analytics, setAnalytics] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <FieldGroup>
        <FieldGroup.Section title="Notifications">
          <Switch label="Push" value={notifications} onValueChange={setNotifications} />
          <Switch label="Email" value={analytics} onValueChange={setAnalytics} />
        </FieldGroup.Section>

        <FieldGroup.Section title="About">
          <Text>Version 1.0.0</Text>
        </FieldGroup.Section>
      </FieldGroup>
    </Host>
  );
}
```

### Custom section header and footer

Use `FieldGroup.SectionHeader` and `FieldGroup.SectionFooter` to render fully styled header/footer slots in place of the default `title` text.

```tsx
import { useState } from 'react';
import { Host, FieldGroup, Switch, Text } from '@expo/ui';

export default function FieldGroupSlotsExample() {
  const [enabled, setEnabled] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <FieldGroup>
        <FieldGroup.Section>
          <FieldGroup.SectionHeader>
            <Text textStyle={{ fontSize: 16, fontWeight: '700' }}>Privacy</Text>
          </FieldGroup.SectionHeader>

          <Switch label="Share usage" value={enabled} onValueChange={setEnabled} />

          <FieldGroup.SectionFooter>
            <Text textStyle={{ fontSize: 12, color: '#8E8E93' }}>
              Helps us improve the app. You can disable this at any time.
            </Text>
          </FieldGroup.SectionFooter>
        </FieldGroup.Section>
      </FieldGroup>
    </Host>
  );
}
```

## API

```tsx
import { FieldGroup } from '@expo/ui';
```

## Components

### `FieldGroup`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[FieldGroupProps](#fieldgroupprops)\>

A scrollable container for grouped settings-style rows, mirroring the look of an iOS Settings screen. Render one or more [`FieldGroup.Section`](#fieldgroupsection) components inside. Direct non-section children are automatically grouped into an implicit section, matching SwiftUI `Form` behavior.

Props for the [`FieldGroup`](#fieldgroup) component, a scrollable container of grouped settings-style rows.

FieldGroupProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A collection of [`FieldGroup.Section`](#fieldgroupsection) components that make up the group. Non-section children are rendered inline between sections, matching SwiftUI `Form` behavior.

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is disabled. Disabled components do not respond to user interaction.

### `hidden`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is hidden.

### `modifiers`

Supported platforms: Android, iOS.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. A modifier supplied here replaces any modifier of the same type that the component derives from `style` or other props.

### `onAppear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component appears on screen.

### `onDisappear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is removed from screen.

### `onPress`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is pressed.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `FieldGroup.Section`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[FieldSectionProps](#fieldsectionprops)\>\>

Props for the [`FieldGroup.Section`](#fieldgroupsection) component, a grouped list of rows within a [`FieldGroup`](#fieldgroup).

FieldSectionProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The rows of the section, optionally interleaved with a single `<FieldGroup.SectionHeader>` and/or `<FieldGroup.SectionFooter>` child to customize the header / footer slots.

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is disabled. Disabled components do not respond to user interaction.

### `hidden`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is hidden.

### `modifiers`

Supported platforms: Android, iOS.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. A modifier supplied here replaces any modifier of the same type that the component derives from `style` or other props.

### `onAppear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component appears on screen.

### `onDisappear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is removed from screen.

### `onPress`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is pressed.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `title`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

A plain-text section title, rendered as the default styled header above the group. Ignored when a `<FieldGroup.SectionHeader>` child is provided.

### `titleUppercase`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the default `title` header is rendered in uppercase. Ignored when a `<FieldGroup.SectionHeader>` child is provided, and ignored on iOS (SwiftUI `Form` decides the header case based on the list style).

### `FieldGroup.SectionFooter`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[FieldSectionFooterProps](#fieldsectionfooterprops)\>\>

Props for the [`FieldGroup.SectionFooter`](#fieldgroupsectionfooter) slot marker.

FieldSectionFooterProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content rendered as the section's footer.

### `FieldGroup.SectionHeader`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[FieldSectionHeaderProps](#fieldsectionheaderprops)\>\>

Props for the [`FieldGroup.SectionHeader`](#fieldgroupsectionheader) slot marker.

FieldSectionHeaderProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content rendered as the section's header.

## Methods

### `FieldGroup.getFieldItemPosition(index, total)`

Supported platforms: Android, iOS, Web.

| Parameter | Type |
| --- | --- |
| `index` | `number` |
| `total` | `number` |

  

Computes the position of a row given its index within a section of `total` rows.

Returns: `FieldItemPosition`

## Types

### `FieldItemPosition`

Supported platforms: Android, iOS, Web.

Literal Type: `string`

Position of a row within a [`FieldGroup.Section`](#fieldgroupsection), used to compute grouped-list corner radii.

Acceptable values are: `'leading'` | `'middle'` | `'trailing'` | `'only'`
